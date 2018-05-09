#!/usr/bin/python
import os
import sys
import cgi
import re
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
import GoogleBooksApiHandler as GBooks
import languages as Lang
from pprint import pprint

def returnErrorMessage(text):
    print("<error>{text}</error>".format(text=text))
    exit(0)

def validateISBN(text):
    if re.match(r'[0-9]+X?',text)==None:
        returnErrorMessage("Your does not match the syntax.")
    if GBooks.searchForBookByISBN(text) != 1:
        returnErrorMessage("Your ISBN is could not be found.")

# TODO check isbn and complete with isbn
def validateStandardTextField(text,field,foundISBN):
    if re.match(r'[a-zA-Z0-9-\'\"` ]+',text)==None:
        returnErrorMessage("Your {field} is invalid.".format(field=field))

def validateLanguage(text):
    languages = Lang.getLanguages()
    if text not in languages:
        returnErrorMessage("Your language is invalid.")

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

isbn = arguments['isbn'].value
author = arguments['author'].value
title = arguments['title'].value
language = arguments['language'].value
thumbnail = arguments['thumbnail'].value
genresText = arguments['genres'].value
interestedInBooksText = arguments['interestedInBooks'].value
interesteInGenresText = arguments['interestedInGenres'].value
expirationDateText = arguments['expirationDate'].value

validateLanguage(language)
if thumbnail=="":
    thumbnail = "https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg"
validateThumbnail(thumbnail)
validateDate(expirationDateText)
if isbn!="":
    validateISBN(isbn)
    validateStandardTextField(author,'author',True)
    validateStandardTextField(title,'title',True)
else:
    validateStandardTextField(author,'author',False)
    validateStandardTextField(title,'title',False)
