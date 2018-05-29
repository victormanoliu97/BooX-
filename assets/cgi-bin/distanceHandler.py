import os
import sys
import cgi
import re
sys.path.append('../server')
import json

def returnErrorMessage(text):
    response = {}
    response['type'] = 'error'
    response['message'] = text
    print(json.dumps(response))
    exit(0)

def returnSuccesMessage():
    response = {}
    response['type'] = 'success'
    response['message'] = 'Your location has been uploaded to our database.'
    print(json.dumps(response))
    exit(0)


print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'].value.encode('utf-8'))


if 'latitude' not in jsonObj.keys():
    returnErrorMessage("Your latitude is not present in the json")
if 'longitude' not in jsonObj.keys():
    returnErrorMessage('Your longitude is not present in the json')

email = jsonObj['email']
latitude = jsonObj['latitude']
longitude = jsonObj['longitude']


import databaseManager as DB
if(DB.findUserByEmail(email)!=None):
    DB.updateUserLocation(email,longitude,latitude)
