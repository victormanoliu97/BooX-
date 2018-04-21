import re
import cx_Oracle
import json
import os
import consolemenu
# data = ''
# with open('countries.json','r') as file:
#     data = data + file.read().replace('name','"name"').replace('code','"code"').replace('\'','\"')
#     print(data)
# with open('countries.json','w') as file:
#     file.write(data)


genresFile = os.path.join(os.path.dirname(__file__),'countries.json')
genres = []
with open(genresFile,'r') as file:
    genres = json.load(file)


conn = cx_Oracle.connect('STUDENT/STUDENT@localhost:1521',encoding = "UTF-8")
cursor = conn.cursor()
querystring = '''drop table tari'''
cursor.execute(querystring)
querystring = '''create table tari(id number, nume varchar(64))'''
cursor.execute(querystring)
for i in range(0,len(genres)):
    print(genres[i]['name'])
    querystring = '''insert into tari values({id},'{genre}')'''.format(id=i+1,genre=genres[i]['name'].replace("'","''"))
    print(querystring)
    cursor.execute(querystring)
conn.commit()