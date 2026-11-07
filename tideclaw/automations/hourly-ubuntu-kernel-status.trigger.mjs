try {
 const r = await web_fetch({url:"https://ubuntu.com/security/CVE-2026-98432",extractMode:"markdown",maxChars:8000});
 if (r.status !== 200) throw new Error("HTTP " + r.status);
 const flat=r.text.replace(/\s+/g," ");
 const start=flat.indexOf("linux |");
 const end=flat.indexOf("linux-hwe",start);
 if(start<0 || end<0) throw new Error("Cannot identify linux package section");
 const match=flat.slice(start,end).match(/26\.04(?: LTS)? resolute\s*\|\s*(.*?)\s+24\.04/);
 if(!match || !match[1]) throw new Error("Cannot parse Ubuntu 26.04 kernel status");
 const status=match[1].trim();
 const previous=trigger.state?.status ?? "Vulnerable work in progress in 7.0.0-43.43";
 json({fire:status!==previous || Boolean(trigger.state?.error),message:"Ubuntu CVE-2026-98432 linux / 26.04 status: "+status+". Previous: "+previous+". Verify official advisory and distinguish proposed testing from released updates. Source: https://ubuntu.com/security/CVE-2026-98432",state:{status,checkedAt:r.fetchedAt,error:false}});
} catch(e) {
 json({fire:true,message:"Kernel status monitor could not verify the advisory: "+String(e)+". Report a monitoring blocker, not a release.",state:{...(trigger.state ?? {}),error:true}});
}
