import sys
sys.path.append('../server')
import databaseManager as dbMan 
import json
import cgi
import xssValidation as xss
from sqlInjectionValidator import validate

print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'].value)

def returnErrorMessage(text):
    response = {}
    response['type'] = 'error' 
    response['message'] = text
    print(json.dumps(response))
    exit(0)

def returnSucces():
    response = {}
    response['type'] = 'success'

    topic = jsonObj['topic']
    language = jsonObj['language']
    max_distance = jsonObj['max_distance'] 

    response['message'] = dbMan.getOffers(topic, language, max_distance)
    print(json.dumps(response))
    exit(0)

topic = jsonObj['topic']
language = jsonObj['language']
max_distance = jsonObj['max_distance'] 

if 'topic' not in jsonObj.keys():
    returnErrorMessage("No ISBN field found.")
if 'language' not in jsonObj.keys():
    returnErrorMessage("No author field found.")
if 'max_distance' not in jsonObj.keys():
    returnErrorMessage("No title field found.")

if (not isinstance(jsonObj['topic'], str)):
    returnErrorMessage("You must enter text here")
if (not isinstance(jsonObj['language'], str)):
    returnErrorMessage("You must enter text here")   

if validate(jsonObj['topic']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['language']) == False:
    returnErrorMessage("You have tried to sql inject")


if (not xss.validate(topic)):
    returnErrorMessage("You have no power here, you xss injector")
if (not xss.validate(language)):
    returnErrorMessage("You have no power here, you xss injector")

returnSucces()

