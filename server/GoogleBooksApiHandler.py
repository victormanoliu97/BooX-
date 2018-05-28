import os
import urllib.request
import urllib.parse
import json
import languages as langs
from io import StringIO
from pprint import pprint

# def searchForBook(name):
#     ApiResponse = urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?&'+urllib.parse.urlencode({'q':name})).read()
#     jsonRoot = json.loads(ApiResponse)
#     totalResults = jsonRoot['totalItems']
#     for child in jsonRoot:
#         print(child)
#     print(totalResults)

def getInfoAboutBook(jquery):
    information = {}
    if 'authors' in jquery['volumeInfo']:
        information['author'] = jquery['volumeInfo']['authors']
    else:
        information['author'] = ''
    if 'title' in jquery['volumeInfo']:
        information['title'] = jquery['volumeInfo']['title']
    else:
        information['title'] = ''
    if 'categories' in jquery['volumeInfo']:
        information['genres'] = jquery['volumeInfo']['categories']
    else:
        information['genres'] = []
    if 'industryIdentifiers' in jquery['volumeInfo']:
        isbnList = jquery['volumeInfo']['industryIdentifiers']
        information['isbn13'] = None
        information['isbn10'] = None
        for entry in isbnList:
            if entry['type']=='ISBN_13':
                information['isbn13']=entry['identifier']
            elif entry['type']=='ISBN_10':
                information['isbn10']=entry['identifier']
    else:
        information['industryIdentifiers'] = ''
    if 'imageLinks' in jquery['volumeInfo']:
        information['smallImage'] = jquery['volumeInfo']['imageLinks']['smallThumbnail']
    else:
        information['smallImage'] = 'https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg'
    if 'imageLinks' in jquery['volumeInfo']:
        information['bigImage'] = jquery['volumeInfo']['imageLinks']['thumbnail']
    else:
        information['bigImage'] = 'https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg'
    if 'language' in jquery['volumeInfo']:
        information['language'] = langs.getLanguageFromRegion(jquery['volumeInfo']['language'])
    else:
        information['language'] = ''
    return information


def searchForBookByISBN(isbn):
    ApiResponse = urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?&'+urllib.parse.urlencode({'q':'isbn:'+isbn})).read()
    jsonRoot = json.loads(ApiResponse)
    totalResults = jsonRoot['totalItems']
    if totalResults==0:
        return (0,None)
    elif totalResults==1:
        return (1,jsonRoot['items'][0])
    else:
        return (len(jsonRoot['items']),jsonRoot['items'])

def searchForBookByName(name):
    ApiResponse = urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?&'+urllib.parse.urlencode({'q':'name:'+name})).read()
    jsonRoot = json.loads(ApiResponse)
    totalResults = jsonRoot['totalItems']
    if totalResults==0:
        return (0,None)
    elif totalResults==1:
        return (1,jsonRoot['items'][0])
    else:
        return (len(jsonRoot['items']),jsonRoot['items'])

if __name__=='__main__':
    pprint(getInfoAboutBook(searchForBookByISBN("9781119249429")))
    # pprint(searchForBookByISBN("9781119249429"))