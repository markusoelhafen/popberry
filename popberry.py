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

def hueLights():
    rooms = hue.getRooms()
    for key, val in rooms.items():
        roomlights = {}

        for light in val['lights']:
            lightdetail = hue.getLightDetails(light)
            roomlights.update({light: lightdetail})

        # print(rooms[key]['lights'])
        rooms[key]['lights'] = roomlights

    return rooms

def updateInformation():
    print('updating information...')
    data['currentweather'] = weather.currentWeather()
    data['room_temp'] = hueTemperature()
    data['rooms'] = hueLights()
    firebase.updateDatabase(data)

def main():
    updateInformation()

if __name__ == '__main__':
    main()
