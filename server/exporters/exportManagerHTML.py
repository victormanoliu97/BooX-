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
