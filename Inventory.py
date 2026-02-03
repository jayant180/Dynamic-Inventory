#!/usr/bin/env python3
import json

host_data=[
  {"name": "web1", "ip": "127.0.0.1", "env": "dev", "role": "web"},
  {"name": "web2", "ip": "127.0.0.2", "env": "qa", "role": "web"},
  {"name": "db1", "ip": "127.0.0.3", "env": "prod", "role": "db"}]

inventory = { "_meta": {"hostvars":{}} }

for host in host_data:
  hostname = host["name"]
  env = host["env"]
 
  if env not in inventory:
    inventory[env] = {"hosts":[]}
 
  inventory[env]["hosts"].append(hostname)
 
  #adding host details(host variables)
 
  inventory["_meta"]["hostvars"][hostname] = { 
    "ansible_host": host["ip"],
    "env": env,
    "role": host["role"]
  }
print(json.dumps(inventory, indent=2))
