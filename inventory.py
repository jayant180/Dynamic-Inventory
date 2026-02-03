#!/usr/bin/env python3
import json
inventory = {
  "web": {
    "hosts": ["web1", "web2"]
  },
  "db": {
    "hosts": ["db1"]
  },
  "_meta": {
    "hostvars": {
       "web1": {
          "ansible_host": "127.0.0.1",
          "env": "dev",
          "role": "web"
      },
       "web2": {
          "ansible_host": "127.0.0.2",
           "env": "prod",
           "role": "web"
      },
       "db1": {
          "ansible_host": "127.0.0.3",
          "env": "qa",
          "role": "db"
      }
    }
  }
}
print(json.dumps(inventory, indent=2))
