import { createServer } from "node:http";
import { pathToFileURL } from "node:url";
import { Firestore } from "@google-cloud/firestore";
import { GoogleAuth, OAuth2Client } from "google-auth-library";
import {
  APPROVERS,
  ApprovalRequestError,
  approvalCard,
  handleChat,
  parseRequest,
  settleDecision,
} from "./service.mjs";

export class FirestoreStore {
  constructor(db) {
    this.db = db;
  }
  approver(email) {
    return this.db.collection("approvers").doc(email);
  }
  request(id) {
    return this.db.collection("requests").doc(id);
  }
  async enroll(email, userId, space) {
    if (!/^spaces\/[A-Za-z0-9_-]+$/u.test(space ?? "")) {
      throw new Error("Invalid DM space.");
    }
    await this.db.runTransaction(async (tx) => {
      const ref = this.approver(email);
      const existing = (await tx.get(ref)).data();
      if (existing && existing.userId !== userId) {
        throw new Error("Stable user ID changed. Administrator intervention required.");
      }
      tx.set(ref, { userId, space });
    });
  }
  async create(request) {
    return this.db.runTransaction(async (tx) => {
      const ref = this.request(request.requestId);
      const existing = (await tx.get(ref)).data();
      if (existing && existing.digest !== request.digest) {
        throw new ApprovalRequestError(
          "REQUEST_ID_CONFLICT",
          409,
          "Request ID already binds different contents. Create a new request ID for changed contents.",
        );
      }
      if (!existing) {
        tx.create(ref, request);
      }
      return existing ?? request;
    });
  }
  async get(id) {
    return (await this.request(id).get()).data();
  }
  async enrollments() {
    return Promise.all(
      APPROVERS.map(async (email) => {
        const data = (await this.approver(email).get()).data();
        return { email, userId: data?.userId, space: data?.space };
      }),
    );
  }
  async decide(actor) {
    return this.db.runTransaction(async (tx) => {
      const ref = this.request(actor.requestId);
      const request = (await tx.get(ref)).data();
      const enrollment = (await tx.get(this.approver(actor.email))).data();
      const result = settleDecision(request, actor, enrollment);
      // Keep the first decision, but retain bounded evidence of the latest attempted action.
      const recorded = {
        ...result,
        lastAttempt: {
          requestedDecision: actor.decision,
          previousState: request.state,
          outcome: result === request ? "unchanged" : "recorded",
          userId: actor.userId,
          receivedAt: new Date(actor.now).toISOString(),
        },
      };
      tx.set(ref, recorded);
      return recorded;
    });
  }
}

export function googleVerifier() {
  const client = new OAuth2Client();
  return async (authorization, audience, allowedEmails) => {
    if (!authorization?.startsWith("Bearer ")) {
      throw new Error("Missing bearer token.");
    }
    const ticket = await client.verifyIdToken({ idToken: authorization.slice(7), audience });
    const claims = ticket.getPayload();
    if (claims?.email_verified !== true || !allowedEmails.includes(claims.email)) {
      throw new Error("Identity is not authorized for this endpoint.");
    }
  };
}

/** Public HTTPS ingress, but every route authenticates its own distinct principal and audience. */
export function createHandler({
  store,
  verify,
  notify,
  baseUrl,
  chatIdentity,
  requesters,
  readers,
}) {
  return async (req, res) => {
    res.setHeader("content-type", "application/json");
    res.setHeader("cache-control", "no-store");
    try {
      const path = new URL(req.url, "http://localhost").pathname;
      const chat = path === "/chat" && req.method === "POST";
      const create = path === "/requests" && req.method === "POST";
      const status = /^\/requests\/([a-f0-9-]{36})$/u.exec(path);
      if (!chat && !create && !(status && req.method === "GET")) {
        res.writeHead(404).end("{}");
        return;
      }
      try {
        await verify(
          req.headers.authorization,
          chat ? `${baseUrl}/chat` : baseUrl,
          chat ? [chatIdentity] : create ? requesters : [...requesters, ...readers],
        );
      } catch {
        res.writeHead(401).end('{"error":"Unauthorized"}');
        return;
      }
      let result;
      if (chat || create) {
        const chunks = [];
        let bytes = 0;
        for await (const chunk of req) {
          bytes += chunk.length;
          if (bytes > 64000) {
            throw new ApprovalRequestError(
              "REQUEST_TOO_LARGE",
              413,
              "Request too large. Shorten the contents and create a new request ID.",
            );
          }
          chunks.push(chunk);
        }
        const value = JSON.parse(Buffer.concat(chunks).toString("utf8"));
        if (chat) {
          const message = await handleChat(value, store, Date.now());
          const operation = value.chat.buttonClickedPayload
            ? "updateMessageAction"
            : "createMessageAction";
          result = { hostAppDataAction: { chatDataAction: { [operation]: { message } } } };
        } else {
          const request = parseRequest(value, Date.now());
          const card = approvalCard(request, `${baseUrl}/chat`);
          if (
            Buffer.byteLength(JSON.stringify(card)) > 32000 ||
            // A decided card adds two metadata widgets and removes one button-list widget.
            card.cardsV2[0].card.sections.reduce(
              (total, section) => total + section.widgets.length,
              0,
            ) > 99
          ) {
            throw new ApprovalRequestError(
              "REQUEST_TOO_LARGE",
              413,
              "Rendered approval card exceeds Google Chat message limit. Shorten request details and create a new request ID.",
            );
          }
          const enrollments = (await store.enrollments()).filter(
            (entry) => entry.userId && entry.space,
          );
          if (enrollments.length === 0) {
            throw new ApprovalRequestError(
              "NO_APPROVERS",
              409,
              "No designated approver has enrolled. Add the app in a private Google Chat DM, then retry the same still-valid immutable request.",
            );
          }
          result = await store.create(request);
          // Deterministic message IDs make retry after partial delivery safe without a queue.
          if (result.state === "pending") {
            const deliveries = await Promise.allSettled(
              enrollments.map((enrollment) => notify(enrollment.space, request)),
            );
            const failed = deliveries.flatMap((delivery, index) => {
              if (delivery.status === "fulfilled") return [];
              const status = delivery.reason?.response?.status;
              return [
                {
                  approverEmail: enrollments[index].email,
                  recovery: status === 403 || status === 404 ? "reenroll" : "retry",
                },
              ];
            });
            const delivered = deliveries.length - failed.length;
            if (delivered === 0) {
              throw new ApprovalRequestError(
                "DELIVERY_FAILED",
                503,
                "Request saved, but no notification delivered. Restore approver DM membership or service access, inspect status, then retry the same still-valid immutable request.",
              );
            }
            // Delivery is a current-attempt projection, never a stored approval decision.
            result = { ...result, delivery: { delivered, failed } };
          }
        }
      } else {
        result = await store.get(status[1]);
        if (!result) {
          res.writeHead(404).end("{}");
          return;
        }
      }
      res.end(JSON.stringify(result));
    } catch (error) {
      // Never expose payloads, tokens, Google error responses, or user content.
      const known = error instanceof ApprovalRequestError;
      const malformed = error instanceof SyntaxError || error instanceof TypeError;
      res.writeHead(known ? error.status : malformed ? 400 : 503).end(
        JSON.stringify({
          code: known ? error.code : malformed ? "INVALID_REQUEST" : "TEMPORARY_FAILURE",
          error: known
            ? error.message
            : malformed
              ? "Invalid request. Correct the contents and use a new request ID if changed."
              : "Service operation failed. Inspect status and repair service access before retrying the same still-valid immutable request.",
        }),
      );
    }
  };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const {
    SERVICE_URL,
    CHAT_SERVICE_ACCOUNT,
    REQUESTER_EMAILS,
    READER_EMAILS = "",
    PORT = "8080",
  } = process.env;
  if (
    !SERVICE_URL ||
    new URL(SERVICE_URL).protocol !== "https:" ||
    SERVICE_URL.endsWith("/") ||
    !/^service-[0-9]+@gcp-sa-gsuiteaddons\.iam\.gserviceaccount\.com$/u.test(
      CHAT_SERVICE_ACCOUNT ?? "",
    ) ||
    !REQUESTER_EMAILS
  ) {
    throw new Error("Explicit service URL, Chat principal and requester identities required.");
  }
  const auth = new GoogleAuth({ scopes: ["https://www.googleapis.com/auth/chat.bot"] });
  const handler = createHandler({
    store: new FirestoreStore(new Firestore()),
    verify: googleVerifier(),
    baseUrl: SERVICE_URL,
    chatIdentity: CHAT_SERVICE_ACCOUNT,
    requesters: REQUESTER_EMAILS.split(","),
    readers: READER_EMAILS.split(",").filter(Boolean),
    notify: async (space, request) => {
      const client = await auth.getClient();
      try {
        await client.request({
          method: "POST",
          url: `https://chat.googleapis.com/v1/${space}/messages`,
          params: { messageId: `client-${request.requestId}` },
          data: approvalCard(request, `${SERVICE_URL}/chat`),
        });
      } catch (error) {
        if (error?.response?.status !== 409) {
          throw error;
        }
      }
    },
  });
  createServer((req, res) => {
    void handler(req, res);
  }).listen(Number(PORT), "0.0.0.0");
}
