import cx_Oracle
import os 
from io import StringIO
import plotly as py
import plotly.graph_objs as go 

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages
from exportManager import userReport

data = [go.Bar(
    x = ['Number of genres', 'Number of languages', 'Number of offers'],
    y = [userReport[0], userReport[1], userReport[2]]
)]

py.offline.plot(
    data, filename='../../assets/reports/report.html'    
)


# html_string = """
# <!DOCTYPE html>
# <html>
#     <head>
#     <meta charset="UTF-8">
#     <title>HTML-REPORT</title>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <style>body{ margin:0 100; background:whitesmoke; }</style>
#     </head>
#     <body>
#         <h1>Reports so far for Offers, Languages and Genres </h1>
#         <ul>
#         <li>Number of genres:""" + userReport[0] + """
#         <li>Number of languages:""" + userReport[1] + """
#         <li>Number of offers:""" + userReport[2] + """
#         <li>Genres existing:""" + str(userReport[3]) + """
#         <ul>
#     </body>
# </html>"""

# f = open("../../assets/reports/report.html", 'w')
# f.write(html_string)
# f.close()

# import webbrowser
# webbrowser.open("report.html")