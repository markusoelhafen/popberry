import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('./config.ini')

IP = parser.get('hue', 'hue_local_ip')
USER = parser.get('hue', 'hue_user')
TEMPSENSOR = parser.get('hue', 'temp_sensor')
BASEURL = "http://" + IP + "/api/" + USER

def getSensors():
    geturl = BASEURL + "/sensors/"
    g = requests.get(geturl)
    return g.json()

def getLights():
    geturl = BASEURL + "/lights/"
    g = requests.get(geturl)
    return g.json()

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
