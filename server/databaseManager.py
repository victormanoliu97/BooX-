import cx_Oracle
import json
import os
import consolemenu
import languages
def sampleOracleConnection():
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    querystring = "select * from topics"
    cursor.execute(querystring)
    row = cursor.fetchone()
    print(row)

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

#def addOffer(bookId,)

def addBook(title,author,isbn,language,topics):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()

    querystring = '''select max(id) from books'''
    cursor.execute(querystring)
    bookId = cursor.fetchone()[0]
    if bookId!=None:
        bookId = bookId + 1
    else:
        bookId = 1
    
    querystring = '''select id from languages where language='{language}' '''.format(language=language)
    cursor.execute(querystring)
    langId = cursor.fetchone()[0]
    if langId!=None:
        langId = langId + 1
    else:
        langId = 0 #if not found, make it unknown

    querystring = '''insert into books (id,title,author,isbn,languageid) values ({id},'{title}','{author}','{isbn}','{language}')'''.format(
        id=bookId,title=title,author=author,isbn=isbn,language=langId)
    cursor.execute(querystring)

    for topic in topics:
        querystring = '''select id from topics where name='{topic}' '''.format(topic=topic)
        cursor.execute(querystring)
        topicId = cursor.fetchone()[0]
        if topicId!=None:
            topicId = topicId
        else:
            topicId = 0 #if not found, make it unknown

        querystring = '''insert into topics_lists (book_id,topic_id) values({bookId},{topicId})'''.format(bookId=bookId,topicId=topicId)
        cursor.execute(querystring)
    conn.commit()
    return bookId


if __name__=='__main__':
    addBook('Perete','Costel','','Afrikaans',["Computers", "Technology & Engineering"])
    # menu = consolemenu.ConsoleMenu("BooX", "Database Manager")
    # fastBuilder = consolemenu.items.FunctionItem("Build Database In One Shot",buildAnything)
    # incrementalBuilderMenu = consolemenu.ConsoleMenu("Build the database step by step")
    # incrementalTopics = consolemenu.items.FunctionItem('Build Topics Table',buildTopics)
    # incrementalLanguages = consolemenu.items.FunctionItem('Build Languages Table',buildLanguages)
    
    # incrementalBuilderMenu.append_item(incrementalTopics)
    # incrementalBuilderMenu.append_item(incrementalLanguages)

    # incrementalBuilder = consolemenu.items.SubmenuItem("Build Database incrementally", submenu=incrementalBuilderMenu)

    # menu.append_item(fastBuilder)
    # menu.append_item(incrementalBuilder)

    # menu.start()
    # menu.join()

