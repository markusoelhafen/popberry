#!/usr/local/bin/python3

import pyrebase

config = {
  "apiKey": "AIzaSyA7vu2G0FdYDbBHz2meKvJTwoCk4Eq7y5M",
  "authDomain": "popberry-11c0b.firebaseapp.com",
  "databaseURL": "https://popberry-11c0b.firebaseio.com",
  "storageBucket": "popberry-11c0b.appspot.com",
  "serviceAccount": "./popberry-b68394b02e78.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("oelhafenmarkus@gmail.com", "67aq87x15")

print(user)
