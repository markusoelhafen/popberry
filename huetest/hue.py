import requests
import json

from ConfigParser import SafeConfigParser

####################
# READ CONFIG FILE #
####################

parser = SafeConfigParser()
parser.read('config.ini')

IP = parser.get('config', 'ip')
USER = parser.get('config', 'user')
LIGHT = parser.get('config', 'light')
SATURATION = parser.get('config', 'lamp_sat')
BRIGHTNESS = parser.get('config', 'lamp_bri')
HUE = parser.get('config', 'lamp_hue')


#generate api urls
geturl = "http://" + IP  + "/api/" + USER  + "/lights/" + LIGHT
puturl = "http://" + IP  + "/api/" + USER  + "/lights/" + LIGHT  + "/state"

#print "puturl: " + puturl

#define json requests
data_on = {"on":True}
data_on["sat"] = SATURATION
data_on["bri"] = BRIGHTNESS
data_on["hue"] = HUE

data_off = {"on":False}

#get request from api
g = requests.get(geturl)

#print g
#print g.json()['state']['on']

if g.json()['state']['on']: #if light is already on -> turn off
    r = requests.put(puturl, json.dumps(data_off), timeout=5)
else: #else light is off -> turn on
    r = requests.put(puturl, json.dumps(data_on), timeout=5)

# i am the test comment
