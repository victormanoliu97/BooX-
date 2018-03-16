import cx_Oracle
import json
import os
import consolemenu
def sampleOracleConnection():
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    querystring = "select * from books"
    cursor.execute(querystring)
    print(cursor)

def buildAnything():
    buildGenres()
    buildLanguages()

def buildGenres():
    genresFile = os.path.join(os.path.dirname(__file__),'genres.json')
    genres = []
    with open(genresFile,'r') as file:
        genres = json.load(file)
    if len(genres)==0:
        return None


    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''delete from genres'''
    cursor.execute(querystring)
    for i in range(0,len(genres)):
        querystring = '''insert into genres values({id},'{genre}')'''.format(id=i+1,genre=genres[i].replace("'","''"))
        print(querystring)
        cursor.execute(querystring)
    conn.commit()


def buildLanguages():
    languagesFile = os.path.join(os.path.dirname(__file__),'isoLanguages.json')
    languagesDict = {}
    with open(languagesFile,'r',encoding="utf8") as file:
        languagesDict = json.load(file)
    languages = []
    print(languagesDict)
    for language in languagesDict:
        languages.append(languagesDict[language]['name'])

    if len(languages)==0:
        return None


    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''delete from languages'''
    cursor.execute(querystring)
    for i in range(0,len(languages)):
        querystring = '''insert into languages values({id},'{genre}')'''.format(id=i+1,genre=languages[i])
        print(querystring)
        cursor.execute(querystring)
    conn.commit()


if __name__=='__main__':
    menu = consolemenu.ConsoleMenu("BooX", "Database Manager")
    fastBuilder = consolemenu.items.FunctionItem("Build Database In One Shot",buildAnything)
    incrementalBuilderMenu = consolemenu.ConsoleMenu("Build the database step by step")
    incrementalGenres = consolemenu.items.FunctionItem('Build Genres Table',buildGenres)
    incrementalLanguages = consolemenu.items.FunctionItem('Build Languages Table',buildLanguages)
    
    incrementalBuilderMenu.append_item(incrementalGenres)
    incrementalBuilderMenu.append_item(incrementalLanguages)

    incrementalBuilder = consolemenu.items.SubmenuItem("Build Database incrementally", submenu=incrementalBuilderMenu)

    menu.append_item(fastBuilder)
    menu.append_item(incrementalBuilder)

    menu.start()
    menu.join()

