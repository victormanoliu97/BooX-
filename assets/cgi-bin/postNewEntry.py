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


if 'isbn' not in arguments.keys():
    returnErrorMessage("No ISBN field found.")
if 'author' not in arguments.keys():
    returnErrorMessage("No author field found.")
if 'title' not in arguments.keys():
    returnErrorMessage("No title field found.")
if 'language' not in arguments.keys():
    returnErrorMessage("No language field found.")
if 'thumbnail' not in arguments.keys():
    returnErrorMessage("No thumbnail field found.")
if 'genres' not in arguments.keys():
    returnErrorMessage("No genres field found.")
if 'interestedInBooks' not in arguments.keys():
    returnErrorMessage("No interestedInBooks field found.")
if 'interestedInTopics' not in arguments.keys():
    returnErrorMessage("No interestedInTopics field found.")
if 'expirationDate' not in arguments.keys():
    returnErrorMessage("No expirationDate field found.")

if validate(arguments['isbn'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['author'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['title'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['language'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['thumbnail'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['genres'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['interestedInBooks'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['interestedInTopics'].value) == False:
    returnErrorMessage("You have tried to sql inject")
if validate(arguments['expirationDate'].value) == False:
    returnErrorMessage("You have tried to sql inject")

isbn = arguments['isbn'].value
if (!xss.validate(isbn)):
    returnErrorMessage("You have no power here, you xss injector")

interestedInBooks = json.loads(arguments['interestedInBooks'].value)
if (!xss.validate(interestedInBooks)):
    returnErrorMessage("You have no power here, you xss injector")
interesteInTopics = json.loads(arguments['interestedInTopics'].value)
if (!xss.validate(interesteInTopics)):
    returnErrorMessage("You have no power here, you xss injector")
expirationDateText = arguments['expirationDate'].value
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
    author = arguments['author'].value
    if (!xss.validate(author)):
        returnErrorMessage("You have no power here, you xss injector")
    title = arguments['title'].value
    if (!xss.validate(title)):
        returnErrorMessage("You have no power here, you xss injector")
    language = arguments['language'].value
    if (!xss.validate(language)):
        returnErrorMessage("You have no power here, you xss injector")
    thumbnail = arguments['thumbnail'].value
    if (!xss.validate(thumbnail)):
        returnErrorMessage("You have no power here, you xss injector")
    validateLanguage(language)
    if thumbnail=="":
        thumbnail = "https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg"
    validateThumbnail(thumbnail)
    validateStandardTextField(author,'author')
    validateStandardTextField(title,'title')
    

import databaseManager as DB
