#!/usr/bin/python
import os
import sys
import cgi
import re
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
import GoogleBooksApiHandler as GBooks
import languages as Lang
import topics as Tpc
import json
import xssValidation as xss
from pprint import pprint
from sqlInjectionValidator import validate

def returnErrorMessage(text):
    response = {}
    response['type'] = 'error'
    response['message'] = text
    print(json.dumps(response))
    exit(0)

def returnSuccesMessage():
    response = {}
    response['type'] = 'success'
    response['message'] = 'Your submission has been uploaded to our database.'
    print(json.dumps(response))
    exit(0)

def validateISBN(text):
    if not (len(text)==10 or len(text)==13):
        returnErrorMessage("Your ISBN does not have a valid length")
    if len(re.findall(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]([0-9][0-9][0-9])?([0-9]|X)',text))==0:
        returnErrorMessage("Your ISBN does not match the syntax.")
    apiResult = GBooks.searchForBookByISBN(text)
    returnCode = apiResult[0]
    if returnCode != 1:
        returnErrorMessage("Your ISBN is could not be found.")
    book = apiResult[1]
    return GBooks.getInfoAboutBook(book)

# TODO check isbn and complete with isbn
def validateStandardTextField(text,field):
    if re.match(r'[a-zA-Z0-9-\'\"` ]+',text)==None:
        returnErrorMessage("Your {field} is invalid.".format(field=field))

def validateLanguage(text):
    languages = Lang.getLanguages()
    if text not in languages:
        returnErrorMessage("Your language is invalid.")

def validateTopics(objectCollection):
    topics = Tpc.getTopics()
    if len(objectCollection)==0:
        returnErrorMessage("You did not select any topic.")
    for topic in objectCollection:
        if topic not in topics:
            returnErrorMessage("Your topic is invalid.")

def validateInterestedTopics(objectCollection):
    topics = Tpc.getTopics()
    if len(objectCollection)==0:
        returnErrorMessage("You did not select any interested topic.")
    for topic in objectCollection:
        if topic not in topics:
            returnErrorMessage("Your topic is invalid.")

def validateThumbnail(url):
    if url[-4:]=='.gif':
        returnErrorMessage("We do not support GIFs in the thumbnails at the moment.")
    if re.match(r'((http://)|(https://))(.+)((\.jpg)|(\.png))',url)==None:
        returnErrorMessage("Your thumbnail URL does not point to an image.")

def validateDate(dateText):
    if re.match(r'2[0-9][0-9][0-9]-[0-9][0-9]?-[0-9][0-9]?',dateText)==None:
        returnErrorMessage("Your date is invalid.")






print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'].value.encode('utf-8'))



if 'apiKey' not in jsonObj.keys():
    returnErrorMessage("You are not logged in.")
if 'isbn' not in jsonObj.keys():
    returnErrorMessage("No ISBN field found.")
if 'author' not in jsonObj.keys():
    returnErrorMessage("No author field found.")
if 'title' not in jsonObj.keys():
    returnErrorMessage("No title field found.")
if 'language' not in jsonObj.keys():
    returnErrorMessage("No language field found.")
if 'thumbnail' not in jsonObj.keys():
    returnErrorMessage("No thumbnail field found.")
if 'topics' not in jsonObj.keys():
    returnErrorMessage("No topics field found.")
if 'interestedInTopics' not in jsonObj.keys():
    returnErrorMessage("No interestedInTopics field found.")
if 'expirationDate' not in jsonObj.keys():
    returnErrorMessage("No expirationDate field found.")

if validate(jsonObj['apiKey']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['isbn']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['author']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['title']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['language']) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['thumbnail']) == False:
    returnErrorMessage("You have tried to sql inject")
for topic in jsonObj['topics']:
    if validate(topic) == False:
        returnErrorMessage("You have tried to sql inject")
for topic in jsonObj['interestedInTopics']:
    if validate(topic) == False:
        returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['expirationDate']) == False:
    returnErrorMessage("You have tried to sql inject")

isbn = jsonObj['isbn']
if (not xss.validate(isbn)):
    returnErrorMessage("You have no power here, you xss injector")
if (not xss.validate(jsonObj['apiKey'])):
    returnErrorMessage("You have no power here, you xss injector")
interestedInTopics = jsonObj['interestedInTopics']
for topic in interestedInTopics:
    if (not xss.validate(topic)):
        returnErrorMessage("You have no power here, you xss injector")
expirationDateText = jsonObj['expirationDate']
if (not xss.validate(expirationDateText)):
    returnErrorMessage("You have no power here, you xss injector")


validateDate(expirationDateText)
validateInterestedTopics(interestedInTopics)

if isbn!="":
    book = validateISBN(isbn)
    author = book['author']
    title = book['title']
    language = book['language']
    thumbnail = book['smallImage']
else:
    author = jsonObj['author']
    if (not xss.validate(author)):
        returnErrorMessage("You have no power here, you xss injector")
    title = jsonObj['title']
    if (not xss.validate(title)):
        returnErrorMessage("You have no power here, you xss injector")
    language = jsonObj['language']
    if (not xss.validate(language)):
        returnErrorMessage("You have no power here, you xss injector")
    thumbnail = jsonObj['thumbnail']
    if (not xss.validate(thumbnail)):
        returnErrorMessage("You have no power here, you xss injector")
    validateLanguage(language)
    if thumbnail=="":
        thumbnail = "https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg"
    validateThumbnail(thumbnail)
    validateStandardTextField(author,'author')
    validateStandardTextField(title,'title')
    

import databaseManager as DB
bookID = DB.addBook(title,author,isbn,language,jsonObj['topics'],thumbnail)
DB.addOffer(DB.getUserIDByApiKey(jsonObj['apiKey']),bookID,interestedInTopics,expirationDateText)
returnSuccesMessage()
