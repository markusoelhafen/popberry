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
