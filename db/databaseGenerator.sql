create table TOPICS
(
	ID NUMBER not null
		primary key,
	NAME VARCHAR2(64) not null
)
/

create table BOOKS
(
	ID NUMBER not null
		primary key,
	TITLE VARCHAR2(256) not null,
	AUTHOR VARCHAR2(256) not null,
	ISBN VARCHAR2(13) not null,
	ASSIGNED_TOPIC_LIST NUMBER,
	LANGUAGEID NUMBER not null
)
/
create table LANGUAGES
(
	ID NUMBER not null
		primary key,
	LANGUAGE VARCHAR2(128) not null
)
/

create unique index BOOKS_ISBN_UINDEX
	on BOOKS (ISBN)
/

create table TOPICS_LISTS
(
	BOOK_ID NUMBER not null,
	TOPIC_ID NUMBER not null
)
/

create table USERS
(
	ID NUMBER not null
		primary key,
	USERNAME NUMBER not null,
	CREATION_DATE DATE not null,
	LAST_LOGIN DATE not null,
	POS_X FLOAT,
	POS_Y FLOAT
)
/

create unique index USERS_USERNAME_UINDEX
	on USERS (USERNAME)
/

create table OFFERS
(
	ID NUMBER not null
		primary key,
	PROPOSER_ID NUMBER not null,
	BOOK_ID_1 NUMBER not null,
	INTERESTED_BOOK_LIST NUMBER,
	INTERESTED_TOPIC_LIST NUMBER,
	EXPIRATION_DATE DATE not null,
	PROPOSEE_ID NUMBER not null,
	BOOK_ID_2 NUMBER
)
/

create table BOOK_LISTS
(
	LIST_ID NUMBER not null,
	BOOK_ID NUMBER not null
)
/

