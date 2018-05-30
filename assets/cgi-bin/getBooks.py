import sys
sys.path.append('../server')
import databaseManager as DB 
import json
import cgi
import xssValidation as xss
import sqlInjectionValidator as sql
from pprint import pprint
from math import sin, cos, sqrt, atan2, radians

from pprint import pprint

print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

def calculateDistance(lat1, lon1,lat2,lon2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

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
if 'apikey' not in jsonObj.keys():
    jsonObj['apikey'] = ''
if 'search' not in jsonObj.keys():
    jsonObj['search'] = ''
if 'topic' not in jsonObj.keys():
    jsonObj['topic'] = ''
if 'language' not in jsonObj.keys():
    jsonObj['language'] = ''
if 'distance' not in jsonObj.keys():
    jsonObj['distance'] = ''
apiKey = jsonObj['apikey']
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
try:
    max_distance = int(max_distance)
except:
    max_distance = 0
response = {}
result = []
if max_distance>0 and max_distance<=500:
    myId = DB.getUserIDByApiKey(apiKey)
    myPos = DB.getUserPosition(myId)
    otherPositions = DB.getAllUserPositionExcept(myId)
    for otherPos in otherPositions:
        distance = calculateDistance(myPos['x'],myPos['y'],otherPos['x'],otherPos['y'])
        if distance<max_distance:
            result.extend(DB.getOffers(searchLike=search,user=otherPos['id'],filters=[topic,language]))
else:
    result = DB.getOffers(searchLike=search,filters=[topic,language])
response["type"] = 'success'
if len(result)==0:
    response["type"] = 'empty'
response["data"] = result
print(json.dumps(response))
