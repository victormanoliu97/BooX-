import cx_Oracle
import json
import os
import consolemenu
import languages
def sampleOracleConnection():
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    querystring = "select * from books"
    cursor.execute(querystring)
    print(cursor)

def buildAnything():
    buildTopics()
    buildLanguages()

def buildTopics():
    import topics as Tpc 
    topics = Tpc.getTopics()
    print(topics)


    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''delete from topics'''
    cursor.execute(querystring)
    for i in range(0,len(topics)):
        querystring = '''insert into topics values({id},'{topic}')'''.format(id=i+1,topic=topics[i].replace("'","''"))
        print(querystring)
        cursor.execute(querystring)
    conn.commit()


def buildLanguages():
    language = languages.getLanguages()
    if language == None:
        return


    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''delete from languages'''
    cursor.execute(querystring)
    for i in range(0,len(language)):
        querystring = '''insert into languages values({id},'{language}')'''.format(id=i+1,language=language[i])
        print(querystring)
        cursor.execute(querystring)
    conn.commit()


if __name__=='__main__':
    menu = consolemenu.ConsoleMenu("BooX", "Database Manager")
    fastBuilder = consolemenu.items.FunctionItem("Build Database In One Shot",buildAnything)
    incrementalBuilderMenu = consolemenu.ConsoleMenu("Build the database step by step")
    incrementalTopics = consolemenu.items.FunctionItem('Build Topics Table',buildTopics)
    incrementalLanguages = consolemenu.items.FunctionItem('Build Languages Table',buildLanguages)
    
    incrementalBuilderMenu.append_item(incrementalTopics)
    incrementalBuilderMenu.append_item(incrementalLanguages)

    incrementalBuilder = consolemenu.items.SubmenuItem("Build Database incrementally", submenu=incrementalBuilderMenu)

    menu.append_item(fastBuilder)
    menu.append_item(incrementalBuilder)

    menu.start()
    menu.join()

