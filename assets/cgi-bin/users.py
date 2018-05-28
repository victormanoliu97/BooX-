#!/usr/bin/python
import os
import sys
import cgi
import json
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
import databaseManager as DB


print("Content-Type: text/html\n")

print('da')
arguments = cgi.FieldStorage()
print('da')
jsonObj = json.loads(arguments['json'].value)
apiKey = jsonObj['apiKey']
email = jsonObj['email']
print('da')
if(DB.findUserByEmail(email)==None):
    print('da')
    DB.addUser(email,apiKey)
    print('da')
