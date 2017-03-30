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
	print "database created"
	connection.commit()


def get_student(email, password):
	connection = sql_connect()
	cursor = connection.cursor()
	t = (email, password,)
	cursor.execute('SELECT uid FROM students WHERE email=? AND password=?', t)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid Credentials")
	return row[0]