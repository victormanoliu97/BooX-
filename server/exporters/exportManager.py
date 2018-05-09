import cx_Oracle
import os 
from io import StringIO
import datetime

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

userReport = []
genres = {}
genresCount = 0;
languagesCount = 0;
offersCount = 0;

def getGenres():
    cursor.execute("SELECT NAME FROM GENRES")
    genres = cursor.fetchall()
    return str(genres)

def getNumberOfGenres():
    cursor.execute("SELECT COUNT(ID) FROM GENRES")
    genresCount = cursor.fetchall()
    return str(genresCount[0][0])

def getNumberOfLanguages():
    cursor.execute("SELECT COUNT(ID) FROM LANGUAGES")
    languagesCount = cursor.fetchall()
    return str(languagesCount[0][0])

def getNumberOffers():
    cursor.execute("SELECT COUNT(ID) FROM OFFERS")
    offersCount = cursor.fetchall()
    return str(offersCount[0][0])

genresCount = getNumberOfGenres()
languagesCount = getNumberOfLanguages()
offersCount = getNumberOffers()

genres = {str(getGenres())}

userReport.append(genresCount)
userReport.append(languagesCount)
userReport.append(offersCount)
userReport.append(genres)
