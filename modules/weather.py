import requests
import json

OPENWEATHER_URL = 'api.openweathermap.org'
API_KEY = '01d07b295723d5f9ebf168c3ccd2bf04'
REQ_BASE = r"/data/2.5/weather?"
CITY_ID = '2911298'

def currentweather():
    requestUrl = 'http://' + OPENWEATHER_URL + REQ_BASE + 'id=' + CITY_ID + '&units=metric' + '&appid=' + API_KEY
    weatherRequest = requests.get(requestUrl)
    weatherResult = weatherRequest.json()

    weatherInformation = {
        'city': weatherResult['name'],
        'temperature': weatherResult['main']['temp']
        'weather': weatherResult['weather'][0]['main'],
        'description': weatherResult['weather'][0]['description']
    }

    return weatherInformation
