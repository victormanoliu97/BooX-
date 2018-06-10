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

def returnSuccesMessage(id):
    response = {}
    response['type'] = 'success'
    response['message'] = 'Your offer has been hidden from other users.'
    response['id'] = id
    print(json.dumps(response))
    exit(0)


print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'].value.encode('utf-8'))


if 'id' not in jsonObj.keys():
    returnErrorMessage("Offer's id is not present in the json")
if 'apikey' not in jsonObj.keys():
    returnErrorMessage('Your apikey is not present in the json')

book_id = jsonObj['id']
apikey = jsonObj['apikey']


import databaseManager as DB
if(DB.getUserIDByApiKey(apikey)!=None):
    if(DB.checkIfOfferBelongsToUser(book_id,DB.getUserIDByApiKey(apikey))):
        DB.hideOffer(book_id)
        returnSuccesMessage(book_id)
    else:
        returnErrorMessage("You are trying to edit an offer that does not belong to you.")
else:
    returnErrorMessage("You are not logged in.")
