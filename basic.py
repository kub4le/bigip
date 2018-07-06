from f5.bigip import ManagementRoot

# Connect to the BigIP
mgmt = ManagementRoot("10.1.1.245", "admin", "1qaz@WSX")

pools = mgmt.tm.ltm.pools
for pool in pools.get_collection():
    print(pool.name)
    for member in pool.members_s.get_collection():
         print(member.name)

# lista 
modules = mgmt.tm.sys.provision
for module in modules.get_collection():
	print('module: {}, level: {}'.format(module['name'],module['level']))

