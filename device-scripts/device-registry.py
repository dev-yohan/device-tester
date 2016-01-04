import urllib
import urllib2
import yaml
import uuid
import json

def getserial(name):
  # Extract serial from cpuinfo file
  cpuserial = uuid.uuid1()
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

with open('iot_config.yml','r') as f:
    config = yaml.load(f)

print config

name = uuid.uuid1()

serial = getserial(name)

url = config['iot_manager']['url']+'/api/v1/device'

values = {'name':name, 'serial':serial}
headers = {'Authorization':'Token token='+config['iot_manager']['token']}

data = urllib.urlencode(values)
req = urllib2.Request(url,data,headers)
response = urllib2.urlopen(req)

json_response = json.loads(response.read())

target = open('.device_id', 'w')

target.write(str(json_response['response_body']['device']['id']))

print json_response['response_body']['device']['id']