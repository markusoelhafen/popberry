#!/usr/local/bin/python3

from modules import *
from configparser import SafeConfigParser

weather = weather.currentWeather()
print(weather)

lights = hue.getLights()
for light, val in lights.items():
    print(val['name'])

temp = hue.getTemperatureSensors(hue.getSensors())
for sensor, val in temp.items():
    room_name = val['name']
    room_temp = val['state']['temperature']/100
    print(room_name,': ',room_temp)

    #push to database
    firebase.pushToDatabase(room_temp, ['room_temp', room_name])
