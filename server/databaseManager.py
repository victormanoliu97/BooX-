import cx_Oracle
import json
import os
import consolemenu
import languages
import datetime
from pprint import pprint
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

def addOffer(propoeserID,bookID,intrestedInTopics,expirationDate):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
            
    querystring = '''select max(list_id) from TOPICS_INTERSTED_LISTS'''
    cursor.execute(querystring)
    listId = cursor.fetchone()[0]
    if listId!=None:
        listId = listId + 1
    else:
        listId = 1
        
    querystring = '''select max(id) from offers'''
    cursor.execute(querystring)
    offerID = cursor.fetchone()[0]
    if offerID!=None:
        offerID = offerID + 1
    else:
        offerID = 1

    for topic in intrestedInTopics:
        querystring = '''select id from topics where name='{topic}' '''.format(topic=topic)
        cursor.execute(querystring)
        topicId = cursor.fetchone()[0]
        if topicId!=None:
            topicId = topicId
        else:
            topicId = 0 #if not found, make it unknown
            
            querystring = '''insert into TOPICS_INTERSTED_LISTS (LIST_ID,topic_id) values({listId},{topicId})'''.format(listId=listId,topicId=topicId)
            cursor.execute(querystring)

    import datetime
    now = datetime.datetime.now()

    querystring = '''insert into offers (id,PROPOSER_ID,BOOK_ID,INTERESTED_TOPIC_LIST, CREATION_DATE, EXPIRATION_DATE,DONE) values ({id},{PROPOSER_ID},{BOOK_ID_1},{INTERESTED_TOPIC_LIST}, to_Date('{CREATION_DATE}','dd.mm.yyyy'), to_Date('{EXPIRATION_DATE}','yyyy-mm-dd'),0)'''.format(
        id=offerID,PROPOSER_ID=propoeserID,BOOK_ID_1=bookID,INTERESTED_TOPIC_LIST=listId, CREATION_DATE=str(now.day)+'.'+str(now.month)+'.'+str(now.year),  EXPIRATION_DATE=expirationDate)
    cursor.execute(querystring)

    conn.commit()
    return offerID
    
def updateUserLocation(email,x,y):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''update users set pos_x={x}, pos_y={y} where email='{email}' '''.format(x=x,y=y,email=email)
    cursor.execute(querystring) 
    conn.commit()

def updateUserLastLogin(apikey):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''update users set last_login = sysdate where apikey = '{apikey}' '''.format(apikey = apikey)
    cursor.execute(querystring)
    conn.commit()


def addUser(email,apiKey):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()

    querystring = '''select max(id) from users'''
    cursor.execute(querystring)
    userId = cursor.fetchone()[0]
    if userId!=None:
        userId = userId + 1
    else:
        userId = 1
    import datetime
    now = datetime.datetime.now()
    querystring = '''insert into USERS (id,email,apikey,creation_date,last_login) values({id},'{email}','{apikey}',
    to_Date('{creation_date}','dd.mm.yyyy'),to_Date('{last_login}','dd.mm.yyyy'))'''.format(
        id=userId,email=email,apikey=apiKey,creation_date=str(now.day)+'.'+str(now.month)+'.'+str(now.year),last_login=str(now.day)+'.'+str(now.month)+'.'+str(now.year))
    cursor.execute(querystring)
    conn.commit()
    return userId

def findUserByEmail(email):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring="select id from users where email='{email}'".format(email=email)
    cursor.execute(querystring)
    try:
        result = cursor.fetchone()[0]
        return result
    except:
        return None

def addBook(title,author,isbn,language,topics,thumbnail):
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
    langId = cursor.fetchone()
    if langId!=None:
        langId = langId[0]
    else:
        langId = 0 #if not found, make it unknown

    querystring = '''insert into books (id,title,author,isbn,languageid,thumbnail_url) values ({id},'{title}','{author}','{isbn}','{language}','{thumbnail_url}')'''.format(
        id=bookId,title=title,author=author[0],isbn=isbn,language=langId,thumbnail_url=thumbnail)
    cursor.execute(querystring)

    for topic in topics:
        querystring = '''select id from topics where name='{topic}' '''.format(topic=topic)
        cursor.execute(querystring)
        topicId = cursor.fetchone()[0]
        if topicId!=None:
            topicId = topicId
        else:
            topicId = 0 #if not found, make it unknown

        querystring = '''insert into TOPICS_BOOKS_LISTS (book_id,topic_id) values({bookId},{topicId})'''.format(bookId=bookId,topicId=topicId)
        cursor.execute(querystring)
    conn.commit()
    return bookId

def hideOffer(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring="update offers set done=1 where id={id}".format(id=id)
    cursor.execute(querystring)
    conn.commit()


def checkIfOfferBelongsToUser(id,userID):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring="select * from offers where id={id} and PROPOSER_ID={userID}".format(id=id,userID=userID)
    cursor.execute(querystring)
    result = cursor.fetchone()
    if result!= None:
        return True
    return False

def getUserIDByApiKey(key):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring="select ID from users where APIKEY='{key}'".format(key=key)
    cursor.execute(querystring)
    result = cursor.fetchone()
    if result==None:
        return None
    return result[0]

def getUserNotifications(apikey):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring="select LAST_LOGIN from users where APIKEY='{apikey}'".format(apikey = apikey)
    cursor.execute(querystring)
    last_login = cursor.fetchone()[0]

    querystring = "select count(ID) from offers where CREATION_DATE > TO_DATE('{last_login}','yyyy-mm-dd HH24:MI:SS')".format(last_login = last_login)
    cursor.execute(querystring)
    result = cursor.fetchone()
    if result==None:
        return None
    return result[0]

def getOffers(id='',searchLike='',user='',filters=['','']):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    join = ''
    where = ''
    if id!='':
        where = ' and o.id={id}'.format(id=id)
    if user!='':
        join = join + ', users u'
        where = ' and o.proposer_id=u.id and u.id={user}'.format(user=user)
    else:
        where = ' and o.done=0'
    if searchLike!='':  #SearchQuery
        where = where + ''' and (upper(b.title) like '%{search}%' or upper(b.author) like '%{search}%') '''.format(search=searchLike.upper())
    if filters[0]!='':  #Topics
        join = join + ', TOPICS_BOOKS_LISTS t'
        where = where + ' and b.id=t.book_id and t.topic_id={topic}'.format(topic=getTopicId(filters[0]))
    if filters[1]!='':  #Languages
        join = join + ', languages l'
        where = where + " and b.languageid=l.id and l.id={language}".format(language=getLanguageId(filters[1]))
    querystring = '''select o.id, o.proposer_id, o.book_id, o.interested_topic_list, o.expiration_date, o.done from offers o, books b{joins} where o.book_id=b.id {wheres}'''.format(joins=join,wheres=where)
    cursor.execute(querystring)
    cursorResults = cursor.fetchall()
    result = []
    for entry in cursorResults:
        data = {}
        data['id'] = entry[0]
        data['email'] = getUserEmail(entry[1])
        data['book'] = getBook(entry[2])
        data['interested'] = getInterestedTopics(entry[3])
        date = entry[4]
        data['expiration'] = str(date.year)+'-'+str(date.month)+'-'+str(date.day)
        data['done'] = entry[5]
        result.append(data)
    return result

def getInterestedTopics(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring='select t2.name from TOPICS_INTERSTED_LISTS t1, TOPICS t2 where t1.topic_id=t2.id and t1.list_id={id}'.format(id=id)
    cursor.execute(querystring)
    cursorResults = cursor.fetchall()
    topics = []
    for topic in cursorResults:
        topics.append(topic[0])
    return topics

def getBook(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring='select title, author, languageid, THUMBNAIL_URL from books where id={id}'.format(id=id)
    cursor.execute(querystring)
    cursorResult = cursor.fetchone()
    data = {}
    data['title'] = cursorResult[0]
    data['author'] = cursorResult[1]
    data['language'] = getLanguage(cursorResult[2])
    data['thumbnail'] = cursorResult[3]
    return data

def getUserPosition(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring='select id, pos_x, pos_y from users where id={id}'.format(id=id)
    cursor.execute(querystring)
    cursorResult = cursor.fetchone()
    return {'id':cursorResult[0],'x':cursorResult[1],'y':cursorResult[2]}

def getAllUserPositionExcept(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring='select id, pos_x, pos_y from users where id!={id}'.format(id=id)
    cursor.execute(querystring)
    cursorResult = cursor.fetchall()
    result = []
    for entry in cursorResult:
        result.append({'id':entry[0],'x':entry[1],'y':entry[2]})
    return result

def getUserEmail(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring='select email from users where id={id}'.format(id=id)
    cursor.execute(querystring)
    try:
        return cursor.fetchone()[0]
    except:
        return None

def getTopicId(text):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''select id from topics where name='{topic}' '''.format(topic=text)
    cursor.execute(querystring)
    try:
        topicID = cursor.fetchone()[0]
        return topicID
    except:
        return None

def getLanguageId(text):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''select id from languages where language like'%{language}%' '''.format(language=text)
    cursor.execute(querystring)
    try:
        langaugeID = cursor.fetchone()[0]
    except:
        return None
    return langaugeID

def getLanguage(id):
    conn = cx_Oracle.connect('TW/TWBooX@localhost:1521',encoding = "UTF-8")
    cursor = conn.cursor()
    querystring = '''select language from languages where id={id}'''.format(id=id)
    cursor.execute(querystring)
    try:
        langaugeID = cursor.fetchone()[0]
        return langaugeID
    except:
        return None

if __name__=='__main__':
    # addUser('pandaismyname1@localhost.com','cevaCod007')
    # updateUserLocation('pandaismyname1@localhost.com',23.5332,12.4432)
    addBook('Perete','Costel','','Afrikaans',["Computers", "Technology & Engineering"],"https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg")
    addBook('Amintiri din Copilarie','Ion Creanga','','Romanian, Moldavian, Moldovan', ["Fable"],"https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg")
    addBook('Ion','Liviu Rebreanu','','Romanian, Moldavian, Moldovan',["Classic"],"https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg")
    addBook('Baltagul','Mihail Sadoveanu','','Romanian, Moldavian, Moldovan',["Folklore"],"https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg")
    addBook('Close to Heaven','John Wickey','','English',["Mystery"],"https://tauruspet.med.yale.edu/staff/edm42/book-cover1.jpg")



     #addOffer(1,1,["Computers", "Technology & Engineering"],'6.1.2018')
    # menu = consolemenu.ConsoleMenu("BooX", "Database Manager")
    # fastBuilder = consolemenu.items.FunctionItem("Build Database In One Shot",buildAnything)
    # incrementalBuilderMenu = consolemenu.ConsoleMenu("Build the database step by step")
    # incrementalTopics = consolemenu.items.FunctionItem('Build Topics Table',buildTopics)
    # incrementalLanguages = consolemenu.items.FunctionItem('Build Languages Table',buildLanguages)
    
    # incrementalBuilderMenu.append_item(incrementalTopics)
    # incrementalBuilderMenu.append_item(incrementalLanguages)python

    # incrementalBuilder = consolemenu.items.SubmenuItem("Build Database incrementally", submenu=incrementalBuilderMenu)

    # menu.append_item(fastBuilder)
    # menu.append_item(incrementalBuilder)

    # menu.start()
    # menu.join()