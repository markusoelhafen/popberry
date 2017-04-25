import requests
import json
import pyrebase
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('./config.ini')

APIKEY = parser.get('firebase', 'apikey')
AUTHDOMAIN = parser.get('firebase', 'authdomain')
DATABASEURL = parser.get('firebase', 'databaseurl')
STORAGEBUCKET = parser.get('firebase', 'storagebucket')
SERVICEACCOUNT = parser.get('firebase', 'serviceAccount')
FB_USER = parser.get('firebase', 'fb_user')
FB_PWD = parser.get('firebase', 'fb_pwd')

fb_config = {
  "apiKey": APIKEY,
  "authDomain": AUTHDOMAIN,
  "databaseURL": DATABASEURL,
  "storageBucket": STORAGEBUCKET,
  "serviceAccount": SERVICEACCOUNT
}

firebase = pyrebase.initialize_app(fb_config)
auth = firebase.auth()
# authenticate user
user = auth.sign_in_with_email_and_password(FB_USER, FB_PWD)
# initialize database
db = firebase.database()

def main():
    print("firebase running...")
    my_stream = db.stream(stream_handler)

def updateDatabase(data):
    db.set(data, user['idToken'])

def pushToDatabase(data, children):
    path = ''
    for child in children:
        path += "/{}".format(child.strip("/"))
    db.child(path).set(data, user['idToken'])

def stream_handler(message):
    # print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    if message["path"] == "/stream/foo":
        if message["data"] == "quit":
            return this.close()

# my_stream = db.child("posts").stream(stream_handler)

if __name__ == "__main__":
    main()
