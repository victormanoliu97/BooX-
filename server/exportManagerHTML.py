import cx_Oracle
import os 
from io import StringIO

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages


html_string = """
<!DOCTYPE html>
<html>
    <head>
    <meta charset="UTF-8">
    <title>HTML-REPORT</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{ margin:0 100; background:whitesmoke; }</style>
    </head>
    <body>
        <h1>Reports so far for Offers, Languages and Genres </h1>
        <ul>
        <li>Number of genres:""" + getNumberOfGenres() + """
        <li>Number of languages:""" + getNumberOfLanguages() + """
        <li>Number of offers:""" + getNumberOffers() + """
    </body>
</html>"""

f = open("reportHTML.html", 'w')
f.write(html_string)
f.close()

import webbrowser
webbrowser.open("reportHTML.html")