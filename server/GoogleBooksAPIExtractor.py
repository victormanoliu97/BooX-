import GoogleBooksApiHandler
import re
import time
import sys
from pprint import pprint
genres = {}
nouns = []
with open('nouns.txt','r') as file:
    for line in file.readlines():
        line = re.findall(r'([a-zA-Z]+)',line)
        if len(line)!=1:
            continue
        else:
            line = line[0]
            nouns.append(line)

for i in range(int(sys.argv[1]),len(nouns)):
    # print(i)
    i = i + 1
    # print(noun)
    books = GoogleBooksApiHandler.searchForBookByName(nouns[i])[1]
    # print(len(books))
    for book in books:
        # print('\n\n\n\n\n\n')
        info = GoogleBooksApiHandler.getInfoAboutBook(book)
        # print(info)
        for genre in info['genres']:
            genres[genre] = genre
    with open('genres.txt','w') as file:
        for genre in genres:
            file.write(genre)
            file.write('\n')
    print(i)