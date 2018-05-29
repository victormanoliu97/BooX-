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


email = jsonObj['email']
topic = ''
language = ''
search = ''


import databaseManager as DB

if(DB.findUserByEmail(email)!=None):
    user = DB.findUserByEmail(email)


result = DB.getOffers(searchLike=search, user=user[0], filters=[topic,language])
response = {}
response["type"] = 'success'
response["data"] = result
print(json.dumps(response))