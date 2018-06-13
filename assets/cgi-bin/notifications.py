#!/usr/bin/python
import os
import sys
import cgi
import json
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
import databaseManager as DB


print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()
jsonObj = json.loads(arguments['json'].value)

apiKey = jsonObj['apiKey']

response = {}
response['type'] = 'success'
response['message'] = int(DB.getUserNotifications(apiKey))
print(json.dumps(response))
