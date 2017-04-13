import requests
import json

OPENWEATHER_URL = 'api.openweathermap.org'
API_KEY = '01d07b295723d5f9ebf168c3ccd2bf04'
REQ_BASE = r"/data/2.5/weather?"
CITY_ID = '2911298'

REQ_URL = 'http://' + OPENWEATHER_URL + REQ_BASE + 'id=' + CITY_ID + '&units=metric' + '&appid=' + API_KEY

WEATHER_REQ = requests.get(REQ_URL)

WEATHER_RESULT = WEATHER_REQ.json()
# print r.json()
# print '##############'
print WEATHER_RESULT['name']
print WEATHER_RESULT['main']['temp']
print WEATHER_RESULT['weather'][0]['main'] + ' - ' + WEATHER_RESULT['weather'][0]['description']
