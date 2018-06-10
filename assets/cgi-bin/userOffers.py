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


print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()
jsonObj = json.loads(arguments['json'].value)


if('apikey' not in jsonObj):
    returnErrorMessage("You don't have an api key.")
apikey = jsonObj['apikey']
topic = ''
language = ''
search = ''


import databaseManager as DB
user = ""
if(DB.getUserIDByApiKey(apikey)!=None):
    user = DB.getUserIDByApiKey(apikey)
else:
    returnErrorMessage("You are not logged in")


result = DB.getOffers(searchLike=search, user=user, filters=[topic,language])
response = {}
response["type"] = 'success'
response["data"] = result
print(json.dumps(response))