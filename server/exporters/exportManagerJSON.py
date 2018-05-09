import json
import io
import cx_Oracle


from exportManager import getNumberOffers
from exportManager import getNumberOfGenres
from exportManager import getNumberOfLanguages

conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
cursor = conn.cursor()

jsonRaport = {}
jsonRaport = {'numberOffers' : getNumberOffers(),
             'numberOfGenres:' : getNumberOfGenres(),
             'numbberOfLanguages' : getNumberOfLanguages()
             }

with io.open('raportJson.json', 'w', encoding = 'utf8') as outfile:
    str_ = json.dumps(jsonRaport, 
                      indent=3, 
                      sort_keys=True, 
                      separators=(',', ': '),
                      ensure_ascii=False)
    outfile.write(str(str_))
