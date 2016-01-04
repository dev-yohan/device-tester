import time
import os, urlparse
import json
import yaml
import psutil
from mqtt_util import *

mqttc = create_mqtt_client()

with open('.device_id', 'r') as f:
    device_id = f.readline() 

with open('iot_config.yml','r') as f:
    config = yaml.load(f)

print config['mqtt_server']

#url = config['mqtt_server']['url']
url_str = config['mqtt_server']['url']+':'+str(config['mqtt_server']['port'])
parsed_url = urlparse.urlparse(url_str)
port = config['mqtt_server']['port']
username = config['mqtt_server']['username']
password = config['mqtt_server']['password']
channel = 'iot/heartbeat_' + device_id

mqttc.username_pw_set(username, password)

mqttc.connect(parsed_url.hostname, parsed_url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe(channel, 0)

while True:
    #print psutil.cpu_times()[0]
    data = {"timestamp": int(time.time()),
      "user_cpu": str(psutil.cpu_times()[0])  
    }
    mqttc.publish(channel, json.dumps(data))
    time.sleep(1)



