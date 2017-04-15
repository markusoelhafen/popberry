#!/usr/local/bin/python3

import requests
import json
import pyrebase
from configparser import SafeConfigParser


####################
# READ CONFIG FILE #
####################

parser = SafeConfigParser()
parser.read('./config.ini')

#GET FIREBASE CONFIG
APIKEY = parser.get('firebase', 'apikey')
AUTHDOMAIN = parser.get('firebase', 'authdomain')
DATABASEURL = parser.get('firebase', 'databaseurl')
STORAGEBUCKET = parser.get('firebase', 'storagebucket')
SERVICEACCOUNT = parser.get('firebase', 'serviceAccount')
FB_USER = parser.get('firebase', 'fb_user')
FB_PWD = parser.get('firebase', 'fb_pwd')

#GET HUE CONFIG
IP = parser.get('hue', 'ip')
HUE_USER = parser.get('hue', 'hue_user')
TEMPSENSOR = parser.get('hue', 'temp_sensor')

# firebase configuration
fbconfig = {
  "apiKey": APIKEY,
  "authDomain": AUTHDOMAIN,
  "databaseURL": DATABASEURL,
  "storageBucket": STORAGEBUCKET,
  "serviceAccount": SERVICEACCOUNT
}

#initialize firebase
firebase = pyrebase.initialize_app(fbconfig)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password(FB_USER, FB_PWD)

# get reference to database
db = firebase.database()

# HUE
# create get request to receive data from specific sensor
geturl = "http://" + IP + "/api/" + HUE_USER + "/sensors/" + TEMPSENSOR
g = requests.get(geturl)

print(g.json()['config'])

if g.json()['config']['on'] == False:  # temperature sensor needs to be turned on
    r = requests.put(puturl, json.dumps({"on": True}), timeout=5)

#get room temperature and put decimal in right place
room_temp = g.json()['state']['temperature'] / 100
#push temperature to firebase database
db.child("room_temp").child("hallway").set(room_temp, user['idToken'])
