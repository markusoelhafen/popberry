#!/usr/local/bin/python3

import pyrebase
from configparser import SafeConfigParser

####################
# READ CONFIG FILE #
####################

parser = SafeConfigParser()
parser.read('./config.ini')

APIKEY = parser.get('firebase', 'apikey')
AUTHDOMAIN = parser.get('firebase', 'authdomain')
DATABASEURL = parser.get('firebase', 'databaseurl')
STORAGEBUCKET = parser.get('firebase', 'storagebucket')
SERVICEACCOUNT = parser.get('firebase', 'serviceAccount')
USER = parser.get('firebase', 'user')
PWD = parser.get('firebase', 'pwd')

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
