import json
import io
import cx_Oracle


from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages
from exportManager import userReport
from exportManager import userWeeklyReport

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

jsonRaport = {}
jsonRaport = {'Number of genres' : userReport[0],
             'Number of languages:' : userReport[1],
             'Number of offers' : userReport[2],
             'Genres existing' : str(userReport[3]),
             'Number of users' : str(userReport[4]),
             'Number of offers in last week' : str(userWeeklyReport[0])
             }


with io.open('../../assets/reports/report.json', 'w', encoding = 'utf8') as outfile:
    str_ = json.dumps(jsonRaport,
                      indent=3, 
                      sort_keys=True, 
                      separators=(',', ': '),
                      ensure_ascii=False)
    outfile.write(str(str_))
