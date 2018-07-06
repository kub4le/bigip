from f5.bigip import ManagementRoot
mgmt = ManagementRoot("10.1.1.245", "admin", "1qaz@WSX")
#rt_table = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs='')
rt = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "netstat -rn"')
print(rt.commandResult)