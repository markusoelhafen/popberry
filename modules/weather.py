import requests
import json
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('./config.ini')

API_KEY = parser.get('weather', 'openweather_apikey')
CITY = parser.get('weather', 'openweather_city_id')
UNITS = "&units" + parser.get('weather', 'openweather_units')
BASEURL = "http://api.openweathermap.org/data/2.5/weather?id="

def currentWeather():
    requestUrl = BASEURL + CITY + "&appid=" + API_KEY + UNITS
    weatherRequest = requests.get(requestUrl)
    weatherResult = weatherRequest.json()

    weatherInformation = {
        'city': weatherResult['name'],
        'temperature': weatherResult['main']['temp'],
        'weather': weatherResult['weather'][0]['main'],
        'description': weatherResult['weather'][0]['description']
    }

    return weatherInformation
