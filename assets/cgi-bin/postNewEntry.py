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
import xssValidator as xss
from pprint import pprint
from sqlInjectionValidator import validate

def returnErrorMessage(text):
    print("<error>{text}</error>".format(text=text))
    exit(0)

def validateISBN(text):
    if not (len(text)==10 or len(text)==13):
        returnErrorMessage("Your ISBN does not have a valid length")
    if re.match(r'[0-9]+X?',text)==None:
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
    if len(objectCollection):
        returnErrorMessage("You did not select any topic.")
    for topic in objectCollection:
        if topic not in topics:
            returnErrorMessage("Your topic is invalid.")

def validateThumbnail(url):
    if url[-4:]=='.gif':
        returnErrorMessage("We do not support GIFs in the thumbnails at the moment.")
    if re.match(r'((http://)|(https://))(.+)((\.jpg)|(\.png))',url)==None:
        returnErrorMessage("Your thumbnail URL does not point to an image.")

def validateDate(dateText):
    if re.match(r'[0-9][0-9]?\.[0-9][0-9]?.2[0-9][0-9][0-9]',dateText)==None:
        returnErrorMessage("Your date is invalid.")






print("Content-Type: text/html\n")

arguments = cgi.FieldStorage()

jsonObj = {}
if 'json' not in argumets.keys():
    returnErrorMessage("No JSON found.")
jsonObj = json.loads(arguments['json'])



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
if 'genres' not in jsonObj.keys():
    returnErrorMessage("No genres field found.")
if 'interestedInBooks' not in jsonObj.keys():
    returnErrorMessage("No interestedInBooks field found.")
if 'interestedInTopics' not in jsonObj.keys():
    returnErrorMessage("No interestedInTopics field found.")
if 'expirationDate' not in jsonObj.keys():
    returnErrorMessage("No expirationDate field found.")

if validate(jsonObj['isbn'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['author'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['title'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['language'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['thumbnail'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['genres'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['interestedInBooks'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['interestedInTopics'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(jsonObj['expirationDate'].value) == False:
    returnErrorMessage("You have tried to sql inject")

isbn = jsonObj['isbn'].value
if (!xss.validate(isbn)):
    returnErrorMessage("You have no power here, you xss injector")

interestedInBooks = json.loads(jsonObj['interestedInBooks'].value)
if (!xss.validate(interestedInBooks)):
    returnErrorMessage("You have no power here, you xss injector")
interesteInTopics = json.loads(jsonObj['interestedInTopics'].value)
if (!xss.validate(interesteInTopics)):
    returnErrorMessage("You have no power here, you xss injector")
expirationDateText = jsonObj['expirationDate'].value
if (!xss.validate(expirationDateText)):
    returnErrorMessage("You have no power here, you xss injector")


validateDate(expirationDateText)
validateTopics(interesteInTopics)

if isbn!="":
    book = validateISBN(isbn)
    author = book['author']
    title = book['title']
    language = book['language']
    thumbnail = book['smallImage']
else:
    author = jsonObj['author'].value
    if (!xss.validate(author)):
        returnErrorMessage("You have no power here, you xss injector")
    title = jsonObj['title'].value
    if (!xss.validate(title)):
        returnErrorMessage("You have no power here, you xss injector")
    language = jsonObj['language'].value
    if (!xss.validate(language)):
        returnErrorMessage("You have no power here, you xss injector")
    thumbnail = jsonObj['thumbnail'].value
    if (!xss.validate(thumbnail)):
        returnErrorMessage("You have no power here, you xss injector")
    validateLanguage(language)
    if thumbnail=="":
        thumbnail = "https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg"
    validateThumbnail(thumbnail)
    validateStandardTextField(author,'author')
    validateStandardTextField(title,'title')
    

import databaseManager as DB
