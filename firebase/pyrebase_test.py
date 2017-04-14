#!/usr/local/bin/python3

import pyrebase
from configparser import SafeConfigParser

####################
# READ CONFIG FILE #
####################

parser = SafeConfigParser()
parser.read('firebase_config.ini')

APIKEY = parser.get('config', 'APIKEY')
AUTHDOMAIN = parser.get('config', 'AUTHDOMAIN')
DATABASEURL = parser.get('config', 'DATABASEURL')
STORAGEBUCKET = parser.get('config', 'STORAGEBUCKET')
SERVICEACCOUNT = parser.get('config', 'SERVICEACCOUNT')
USER = parser.get('config', 'USER')
PWD = parser.get('config', 'PWD')

config = {
  "apiKey": APIKEY,
  "authDomain": AUTHDOMAIN,
  "databaseURL": DATABASEURL,
  "storageBucket": STORAGEBUCKET,
  "serviceAccount": SERVICEACCOUNT
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password(USER, PWD)

print(user)
