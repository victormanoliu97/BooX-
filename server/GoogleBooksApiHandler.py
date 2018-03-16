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
    # searchForBook("a song of ice and fire")
    print(searchForBookByISBN("9780553897845"))