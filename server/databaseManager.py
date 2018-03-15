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

def buildGenres():
    genresFile = os.path.join(os.path.dirname(__file__),'genres.json')
    genres = []
    with open(genresFile,'r') as file:
        genres = json.load(file)
    if len(genres)==0:
        return None


    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
    cursor = conn.cursor()
    querystring = '''delete from genres'''
    cursor.execute(querystring)
    for i in range(0,len(genres)):
        querystring = '''insert into genres values({id},'{genre}')'''.format(id=i+1,genre=genres[i].replace("'","''"))
        print(querystring)
        cursor.execute(querystring)
    conn.commit()


if __name__=='__main__':
    menu = consolemenu.ConsoleMenu("BooX", "Database Manager")
    fastBuilder = consolemenu.items.MenuItem("Build Database In One Shot")
    incrementalBuilderMenu = consolemenu.ConsoleMenu("Build the database step by step")
    incrementalGenres = consolemenu.items.FunctionItem('Build Genres Table',buildGenres)
    
    incrementalBuilderMenu.append_item(incrementalGenres)

    incrementalBuilder = consolemenu.items.SubmenuItem("Build Database incrementally", submenu=incrementalBuilderMenu)

    menu.append_item(fastBuilder)
    menu.append_item(incrementalBuilder)

    menu.start()
    menu.join()

