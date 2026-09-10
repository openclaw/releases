start_all()
machine.succeed("test ! -e /home/qualification/fixture")
machine.succeed("loginctl enable-linger qualification")
machine.succeed("systemctl start user@1000.service")
machine.wait_for_unit("user@1000.service")
machine.wait_until_succeeds("test -S /run/user/1000/bus")
status, output = machine.execute(
    "su qualification -c '"
    "XDG_RUNTIME_DIR=/run/user/1000 "
    "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus "
    "python3 /etc/source-qualification/probe/probe.py "
    "/etc/source-qualification/inputs.json'"
)
print(output)
assert status == 0, "source package qualification failed"
