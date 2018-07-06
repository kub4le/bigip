import requests
import json

BIGIP_ADDRESS = '10.1.1.245'
BIGIP_USER = 'admin'
BIGIP_PASS = '1qaz@WSX'

#disable insecure ssl warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = requests.session()
s.auth = (BIGIP_USER,BIGIP_PASS)
s.verify = False
s.headers.update({'Content-Type':'application/json'})

BIGIP_URL_BASE = 'https://%s/mgmt/tm' % BIGIP_ADDRESS

#r = b.get('https://10.1.1.245/mgmt/tm/ltm/rule')

#create new pool
#pool members list
pm = ['10.1.20.101:80','10.1.20.102:80']
payload = {}
payload['kind'] = 'tm:ltm:pool:poolstate'
payload['name'] = 'tcb-pool'
payload['members'] = [{'kind':'ltm:pool:members','name': member} for member in pm]
# r = s.post('%s/ltm/pool' % BIGIP_URL_BASE, data = json.dumps(payload))
#
# print r.text

#put
# r = s.put('%s/ltm/pool' % BIGIP_URL_BASE, data=json.dumps(payload))
# print r.text

#list pools
r = s.get('%s/ltm/pool/~Common~tcb-pool/members' % BIGIP_URL_BASE)
print r.text

#add pool member
member['name'] = {"name":"10.1.20.102:80"}
r = s.post('%s/ltm/pool/~Common~tcb-pool/members' % BIGIP_URL_BASE)
print r.text

r = s.get('%s/ltm/pool/~Common~tcb-pool/members' % BIGIP_URL_BASE)
print r.text

#delete pool member
# r = s.delete('%s/ltm/pool/~Common~tcb-pool/members/~Common~10.1.20.102:80' % BIGIP_URL_BASE)
# print r.text
