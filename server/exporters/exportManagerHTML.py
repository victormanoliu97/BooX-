import cx_Oracle
import os 
from io import StringIO
import plotly as py
import plotly.graph_objs as go 
import datetime
from plotly import tools

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages
from exportManager import getNumberUsers
from exportManager import userReport
from exportManager import userWeeklyReport

now = datetime.datetime.now()

xweek = [datetime.datetime(year=now.year, month=now.month, day=now.day - 7),
    datetime.datetime(year=now.year, month=now.month, day=now.day - 6),
    datetime.datetime(year=now.year, month=now.month, day=now.day - 5),
    datetime.datetime(year=now.year, month=now.month, day=now.day - 4),
    datetime.datetime(year=now.year, month=now.month, day=now.day - 3)]

traceAllTime = go.Bar(
    x = ['Number of genres', 'Number of languages', 'Number of offers', 'Number of users'],
    y = [userReport[0], userReport[1], userReport[2], userReport[4]]
)

traceWeekly = go.Scatter(
    x=xweek,
    y=[1, 3, 4, 5, 7]
)

# data = [go.Bar(
#     x = ['Number of genres', 'Number of languages', 'Number of offers', 'Number of users'],
#     y = [userReport[0], userReport[1], userReport[2], 10]
# ),
#     go.Scatter(
#             x=xweek,
#             y=[1, 3, 6])
# ]

# layout = go.Layout(xaxis = dict(
#                    range = [to_unix_time(datetime.datetime(2013, 10, 17)),
#                             to_unix_time(datetime.datetime(2013, 11, 20))]
#     ))

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Raport all time', 
                                                          'Raport saptamanal al ofertelor'))
                                                          
fig.append_trace(traceAllTime, 1, 1)
fig.append_trace(traceWeekly, 1, 2)

fig['layout'].update(height=900, width=900, title='Rapoarte utilizator')

# py.offline.plot(
#     data, filename='../../assets/reports/report.html',auto_open=False
# )

py.offline.plot(fig, filename='../../assets/reports/report.html', auto_open=False
)