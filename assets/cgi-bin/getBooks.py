import sys
sys.path.append('../server')
import databaseManager as DB 
import json
import cgi
import xssValidation as xss
import sqlInjectionValidator as sql

from pprint import pprint

print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

def returnErrorMessage(text):
    response = {}
    response['type'] = 'error' 
    response['message'] = text
    print(json.dumps(response))
    exit(0)

jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'].value)
if 'search' not in jsonObj.keys():
    jsonObj['search'] = ''
if 'topic' not in jsonObj.keys():
    jsonObj['topic'] = ''
if 'language' not in jsonObj.keys():
    jsonObj['language'] = ''
if 'distance' not in jsonObj.keys():
    jsonObj['distance'] = ''
search = jsonObj['search']
topic = jsonObj['topic']
language = jsonObj['language']
max_distance = jsonObj['distance'] 

if (not xss.validate(search)):
    returnErrorMessage("You have no power here, you xss injector")
if (not xss.validate(topic)):
    returnErrorMessage("You have no power here, you xss injector")
if (not xss.validate(language)):
    returnErrorMessage("You have no power here, you xss injector")
if (not xss.validate(max_distance)):
    returnErrorMessage("You have no power here, you xss injector")
if (not sql.validate(search)):
    returnErrorMessage("You have no power here, you sql injector")
if (not sql.validate(topic)):
    returnErrorMessage("You have no power here, you sql injector")
if (not sql.validate(language)):
    returnErrorMessage("You have no power here, you sql injector")
if (not sql.validate(max_distance)):
    returnErrorMessage("You have no power here, you sql injector")

result = DB.getOffers(searchLike=search,filters=[topic,language])
pprint(result)