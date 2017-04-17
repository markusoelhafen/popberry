#!/usr/local/bin/python3

import requests
import json
import pyrebase
from modules import *
from configparser import SafeConfigParser

weather = weather.currentWeather()

print(weather)
