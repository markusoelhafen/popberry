#!/usr/local/bin/python3

from modules import *

data = {}

def hueTemperature():
    temp = hue.getTemperatureSensors(hue.getSensors())

    tempSensors = {}

    for sensor, val in temp.items():
        room_name = val['name']
        room_temp = val['state']['temperature']/100
        tempSensors[room_name] = room_temp

    return tempSensors

def updateInformation():
    print('updating information...')
    data['currentweather'] = weather.currentWeather()
    data['room_temp'] = hueTemperature()
    firebase.updateDatabase(data)

def main():
    # updateInformation()
    rooms = hue.getRooms()
    for key, val in rooms.items():
        print(val['name'])

if __name__ == '__main__':
    main()
