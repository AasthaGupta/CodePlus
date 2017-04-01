import os
import glob
import sqlite3 as sql

database = 'src/database/ojms.db'
connection = None

def sql_init():
	if not os.path.isfile(database):
		global connection
		create_tables()
		create_oj_database()
		connection.close()
		connection = None

def sql_connect():
	global connection
	if connection == None:
		connection = sql.connect(database)
		connection.isolation_level = None
	return connection

def create_tables():
	connection = sql_connect()
	cursor = connection.cursor()
	path = 'src/schema'
	for sqlfilename in glob.glob(os.path.join(path, '*.sql')):
		sqlFile = open(sqlfilename, 'r')
		sqlScript = sqlFile.read()
		sqlFile.close()
		cursor.executescript(sqlScript)
	connection.commit()


def create_oj_database():
	connection = sql_connect()
	cursor = connection.cursor()
	cursor.execute('')
	#to be done
	#here we have to create tables and insert values into it
	#using the files in src/database/create/
	#files in create will have insert queries
	#cursor.executescript() can be used for this
	print "database created"
	connection.commit()

def username_exists(username):
	if username is "" :
		return True
	connection = sql_connect()
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM users WHERE username=?', username)
	return cursor.fetchone() is not None

def email_exists(email):
	if email is "" :
		return True
	connection = sql_connect()
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM users WHERE email=?', email)
	return cursor.fetchone() is not None

def add(username,password,p_fname,p_lname,country,dob):
	connection = sql_connect()
	cursor = connection.cursor()
    	cursor.execute("INSERT INTO person (username,password,p_fname,p_lname,country,dob) VALUES (?,?,?,?,?.?)", (username,password,p_fname,p_lname,country,dob))
	print "user added"
	connection.commit()


def get_user(email, password):
	connection = sql_connect()
	cursor = connection.cursor()
	t = (email, password,)
	cursor.execute('SELECT * FROM students WHERE email=? AND password=?', t)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid Credentials")
	return row
