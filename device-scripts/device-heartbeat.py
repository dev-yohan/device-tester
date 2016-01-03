import time
import os, urlparse
import json
import yaml
import psutil
import paho.mqtt.client as paho

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = paho.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe    

with open('iot_config.yml','r') as f:
    config = yaml.load(f)

print config['mqtt_server']

#url = config['mqtt_server']['url']
url_str = config['mqtt_server']['url']+':'+str(config['mqtt_server']['port'])
parsed_url = urlparse.urlparse(url_str)
port = config['mqtt_server']['port']
username = config['mqtt_server']['username']
password = config['mqtt_server']['password']
channel = 'iot/heartbeat_1'

mqttc.username_pw_set(username, password)

#mqttc.connect(url, int(port))
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



