#!/usr/local/bin/python3

import requests
import json
import pyrebase
from configparser import SafeConfigParser


OPENWEATHER_URL = 'api.openweathermap.org'
API_KEY = '01d07b295723d5f9ebf168c3ccd2bf04'
REQ_BASE = r"/data/2.5/weather?"
CITY_ID = '2911298'

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

def getTempSensor(sensors):
    for sensor, val in sensors.items():
        #print(val['type'])
        if val['type'] == 'ZLLTemperature':
            # print(sensor)
            # print(val)
            return {sensor: val}

# HUE
# create get request to receive data from specific sensor
geturl = "http://" + IP + "/api/" + HUE_USER + "/sensors/" #+ TEMPSENSOR
g = requests.get(geturl)

tempSensors = getTempSensor(g.json())

def pushTempToDatabase(sensors):
    for sensor, val in sensors.items():
        if val['config']['on'] == False:
            print('its off!')

        room_name = val['name']
        room_temp = val['state']['temperature'] / 100
        print(room_name,': ',room_temp)
        #push temperature to firebase database
        db.child("room_temp").child(room_name).set(room_temp, user['idToken'])

pushTempToDatabase(tempSensors)

### WEATHER ACTION

reqUrl = 'http://' + OPENWEATHER_URL + REQ_BASE + 'id=' + CITY_ID + '&units=metric' + '&appid=' + API_KEY
weatherRequest = requests.get(reqUrl)
weatherResult = weatherRequest.json()

db.child("currentweather").child("city").set(weatherResult['name'], user['idToken'])
db.child("currentweather").child("temperature").set(weatherResult['main']['temp'], user['idToken'])
db.child("currentweather").child("weather").set(weatherResult['weather'][0]['main'], user['idToken'])
db.child("currentweather").child("description").set(weatherResult['weather'][0]['description'], user['idToken'])
