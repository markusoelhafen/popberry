#!/usr/local/bin/python3

from modules import *

data = {}

def getWeather():
    return weather.currentWeather()


def hueTemperature():
    temp = hue.getTemperatureSensors(hue.getSensors())

    tempSensors = []

    for sensor, val in temp.items():
        room_name = val['name']
        room_temp = val['state']['temperature']/100
        #print(room_name,': ',room_temp)
        tempSensors.append({room_name : room_temp})

    return tempSensors

def updateInformation():
    data['currentweather'] = weather.currentWeather()
    print(data['currentweather'])
    # push to database
    for key, val in data['currentweather'].items():
        firebase.pushToDatabase(val, ['currentweather', key])

    data['room_temp'] = hueTemperature()
    for d in data['room_temp']:
        for key, val in d.items():
            firebase.pushToDatabase(val, ['room_temp', key])


def main():
    print('main running')
    updateInformation()

if __name__ == '__main__':
    main()
