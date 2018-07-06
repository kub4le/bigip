# the data file must be transferred to the target LTM via scp or something similar
# the file name and full path must match DG_SRC
import requests, json

# define program-wide variables
BIGIP_ADDRESS = '10.1.1.245'
BIGIP_USER = 'admin'
BIGIP_PASS = 'admin'
DG_FILE = 'Data'
DG_SRC1 = 'file:/var/tmp/PreviousData.txt'
DG_TYPE = 'string'
EXT_DG_NAME = 'Data'
DG_SRC2 = 'file:/var/tmp/CurrentData.txt'

# get data-group info
def get_dg(bigip):

        r = bigip.get('%s/ltm/data-group' % BIGIP_URL_BASE)
        print json.dumps(r.json())

def create_sys_file(bigip):
        payload = {}

        payload['name'] = DG_FILE
        payload['separator'] = ':='
        payload['sourcePath'] = DG_SRC1
        payload['type'] = DG_TYPE
        print json.dumps(payload)

        r = bigip.post('%s/sys/file/data-group' % BIGIP_URL_BASE, data=json.dumps(payload))
        print json.dumps(r.json())

def create_ext_dg(bigip):
        payload = {}

        payload['name'] = EXT_DG_NAME
        payload['externalFileName'] = '/Common/%s' % DG_FILE
        print json.dumps(payload)

        r = bigip.post('%s/ltm/data-group/external' % BIGIP_URL_BASE, data=json.dumps(payload))
        print json.dumps(r.json())

def update_sys_file(bigip):
        payload = {}

        payload['name'] = DG_FILE
        payload['separator'] = ':='
        payload['sourcePath'] = DG_SRC2
        print json.dumps(payload)

        r = bigip.put('%s/sys/file/data-group/%s' % (BIGIP_URL_BASE, DG_FILE), data=json.dumps(payload))
        print json.dumps(r.json())

def update_ext_dg(bigip):
        payload = {}

        payload['name'] = EXT_DG_NAME
        print json.dumps(payload)

        r = bigip.put('%s/ltm/data-group/external/%s' % (BIGIP_URL_BASE, DG_FILE), data=json.dumps(payload))
        print json.dumps(r.json())

def save_config(bigip):
        payload = {}

        payload['command'] = 'save'
        print json.dumps(payload)

        r = bigip.post('%s/sys/config' % BIGIP_URL_BASE, data=json.dumps(payload))
        print json.dumps(r.json())

# REST resource for BIG-IP that all other requests will use
bigip = requests.session()
bigip.auth = (BIGIP_USER, BIGIP_PASS)
bigip.verify = False
bigip.headers.update({'Content-Type' : 'application/json'})
print "created REST resource for BIG-IP at %s..." % BIGIP_ADDRESS

# Requests requires a full URL to be sent as arg for every request, define base URL globally here
BIGIP_URL_BASE = 'https://%s/mgmt/tm' % BIGIP_ADDRESS

# get data info
get_dg(bigip)
print "got data group info"

create_sys_file(bigip)
print "created sys file for external data group"

create_ext_dg(bigip)
print "created external data group"

update_sys_file(bigip)
print "updated sys file for external data group"

update_ext_dg(bigip)
print "updated external data group"

save_config(bigip)
print "saved config"
