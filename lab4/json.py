#1
new_data = {
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        }
    ]
}

out = "Interface Status\n"
out += "=" * 80 + "\n"
out += "{:<50} {:<20} {:<6} {:<6}\n".format("DN", "Description", "Speed", "MTU")
out += "-" * 80 + "\n"

for i in new_data["imdata"]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    d = i["l1PhysIf"]["attributes"]["descr"]
    s = i["l1PhysIf"]["attributes"]["speed"]
    m = i["l1PhysIf"]["attributes"]["mtu"]
    out += "{:<50} {:<20} {:<6} {:<6}\n".format(dn, d, s, m)

print(out)
