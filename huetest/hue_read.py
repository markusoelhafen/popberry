import requests
import json

from configparser import SafeConfigParser

####################
# READ CONFIG FILE #
####################

parser = SafeConfigParser()
parser.read('config.ini')

IP = parser.get('config', 'ip')
USER = parser.get('config', 'user')
TEMPSENSOR = parser.get('config', 'temp_sensor')

# generate api urls
geturl = "http://" + IP + "/api/" + USER + "/sensors/" + TEMPSENSOR


# define json requests
#config_on = {"on": True}

# get request from api
g = requests.get(geturl)

# print g
# print g.json()['state']['on']

if g.json()['config']['on']:  # if light is already on -> turn off
    print (g.json()['state']['temperature'])
else:  # else light is off -> turn on
    r = requests.put(puturl, json.dumps({"on": True}), timeout=5)

# i am the test comment
