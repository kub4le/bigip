from f5.bigip import ManagementRoot

mgmt = ManagementRoot('10.1.1.245', 'admin', '1qaz@WSX')

virtuals = mgmt.tm.ltm.virtuals.get_collection()
print(virtuals[0].name)
