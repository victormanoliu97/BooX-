#!/usr/bin/python
import os
import sys
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
sys.path.append('../server')
from subprocess import Popen
import GoogleBooksApiHandler as GBooks
from pprint import pprint


print("Content-Type: text/html\n")
print("yeee boiiii\n\n")
# pprint(GBooks.getInfoAboutBook(GBooks.searchForBookByISBN("9781119249429")))
# print(GBooks.getInfoAboutBook(("9781119249429")))

# Data validifier


arguments = cgi.FieldStorage()
currentSearchField = arguments['field'].value
currentSearchValue = arguments['value'].value

if currentSearchField=='isbn':
    answer = GBooks.searchForBookByISBN(currentSearchValue)
    if answer[0]==0:
        print('No book found')
    elif answer[0]==1:
        print('Found one book')
        GBooks.getInfoAboutBook(answer[1])
    else:
        print('Found more books')
        for i in range(0,answer[0]):
            GBooks.getInfoAboutBook(answer[1][i])
elif currentSearchField=='name':
    GBooks.getInfoAboutBook(GBooks.searchForBookByName(currentSearchValue))
