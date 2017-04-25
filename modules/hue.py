import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('./config.ini')

IP = parser.get('hue', 'hue_local_ip')
USER = parser.get('hue', 'hue_user')
TEMPSENSOR = parser.get('hue', 'temp_sensor')
BASEURL = "http://" + IP + "/api/" + USER

def main():
    print("running main...")

def getSensors():
    geturl = BASEURL + "/sensors/"
    g = requests.get(geturl)
    return g.json()

def getLightDetails(LIGHT):
    geturl = BASEURL + "/lights/" + LIGHT
    g = requests.get(geturl)
    return g.json()

def getLights():
    geturl = BASEURL + "/lights/"
    g = requests.get(geturl)
    return g.json()

def getRooms():
    geturl = BASEURL + "/groups/"
    g = requests.get(geturl)
    groups = g.json()

    allRooms = {}

    for key, val in groups.items():
        if val['type'] == 'Room':
            allRooms.update({key: val})

    return allRooms

# def matchLightsToRooms(allRooms):
#     for key, val in allRooms.items():


def getTemperatureSensors(sensors):
    for sensor, val in sensors.items():
        if val['type'] == 'ZLLTemperature':
            return {sensor: val}

def turnOnLight(LIGHT):
    url = BASEURL + "/lights/" + LIGHT + "/state"
    requests.put(url, json.dumps({"on": True}), timeout=5)

def turnOffLight(LIGHT):
    url = BASEURL + "/lights/" + LIGHT + "/state"
    requests.put(url, json.dumps({"on": False}), timeout=5)

def dimLight(LIGHT, VALUE=None):
    url = BASEURL + "/lights/" + LIGHT
    puturl = url + "/state"
    g = requests.get(url)

    if VALUE:
        targetBrightness = int(254/100*VALUE)
    else:
        currentBrightness = g.json()['state']['bri']
        targetBrightness = currentBrightness - (int(254/10))

    if targetBrightness <= 0:
        turnOffLight(LIGHT)
        print("turning off light")
    else:

        requests.put(puturl, json.dumps({"on": True,"bri": targetBrightness}), timeout=5)


if __name__ == "__main__":
    main()
