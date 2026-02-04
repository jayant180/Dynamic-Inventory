# inventory.py structure
 inventory = {
  "group1": {
    hosts: ["host1", "host2"]
   },
  "group2":{
    "hosts": ["host1", "host2"]
   }
  _meta: { hostvars: { host1: { details } } }
}
Above is the ideal structure for understanding.
group contains hosts
hosts: gets variables from _meta.hostvars
