import os
import urllib.request
import urllib.parse
import json
from io import StringIO

# def searchForBook(name):
#     ApiResponse = urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?&'+urllib.parse.urlencode({'q':name})).read()
#     jsonRoot = json.loads(ApiResponse)
#     totalResults = jsonRoot['totalItems']
#     for child in jsonRoot:
#         print(child)
#     print(totalResults)

def getInfoAboutBook(jquery):
    information = {}
    information['authors'] = jquery['volumeInfo']['authors']
    information['title'] = jquery['subtitle']
    isbnList = jquery['industryIdentifiers']
    information['isbn13'] = None
    information['isbn10'] = None
    for entry in isbnList:
        if entry['type']=='ISBN_13':
            information['isbn13']=entry['identifier']
        elif entry['type']=='ISBN_10':
            information['isbn10']=entry['identifier']
    information['smallImage'] = jquery['imageLinks']['smallThumbnail']
    information['bigImage'] = jquery['imageLinks']['thumbnail']
    information['language'] = jquery['language']
    return information


def searchForBookByISBN(isbn):
    ApiResponse = urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?&'+urllib.parse.urlencode({'q':'isbn:'+isbn})).read()
    jsonRoot = json.loads(ApiResponse)
    totalResults = jsonRoot['totalItems']
    if totalResults==0:
        print('invalid isbn')
        return None
    elif totalResults==1:
        print('found the right book')
        return jsonRoot['items'][0]
    else:
        print('found more books')
        return jsonRoot['items']

if __name__=='__main__':
    print(searchForBookByISBN("95092686410"))