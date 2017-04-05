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
	print "Executed table schema."


def create_oj_database():
	connection = sql_connect()
	cursor = connection.cursor()
	path = 'src/database/data'
	for inputfilename in glob.glob(os.path.join(path, '*.txt')):
		inputFile=open(inputfilename,'r')
		Query=inputFile.readline().rstrip("\n")
		for line in inputFile:
			line=line.rstrip(",;\n")
			insertQuery=Query+line+";"
			cursor.execute(insertQuery)
		connection.commit()
		print "Inserted values into",inputfilename[18:-4]
	print "Database created"

def username_exists(username):
	if username is "" :
		return True
	connection = sql_connect()
	cursor = connection.cursor()
	values=(username,)
	cursor.execute('SELECT * FROM user WHERE username=?', values)
	return cursor.fetchone() is not None

def email_exists(email):
	if email is "" :
		return True
	connection = sql_connect()
	cursor = connection.cursor()
	values=(email,)
	cursor.execute('SELECT * FROM user WHERE email=?', values)
	return cursor.fetchone() is not None

def add(fname,lname,email,username,password,country,dob,oname,otype,ocity,ocountry):
	connection = sql_connect()
	cursor = connection.cursor()
	userInfo = (email,username,password,fname,lname,country,dob,)
	orgInfo = (oname,otype,ocity,ocountry,)
	print userInfo
	cursor.execute("INSERT INTO user (email,username,password,fname,lname,country,dob) VALUES (?,?,?,?,?,?,?)", userInfo)
	print "added into table user"
	cursor.execute("INSERT INTO organisation (oname, otype, ocity, ocountry) VALUES (?,?,?,?)", orgInfo)
	print "added into table organisation"
	connection.commit()
	print "user added"

def addsub(q_code, language, s_time, s_date, status):
	connection = sql_connect()
	cursor = connection.cursor()
	subInfo = (s_date, s_time, language, status)
	print "submission info"
	print subInfo
	cursor.execute("INSERT INTO solution ( sdate, stime, language, status ) VALUES (?,?,?,?)", subInfo)
	cursor.execute("INSERT INTO solution_of ( q_code ) VALUES (?)", q_code)
	connection.commit()
	print "submission added"
	
	


def get_user(email, password):
	connection = sql_connect()
	cursor = connection.cursor()
	values = (email,password,)
	cursor.execute('SELECT * FROM user WHERE email=? and password=?', values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid Credentials")
	return row

def get_user_by_email(email):
	connection = sql_connect()
	cursor = connection.cursor()
	values = (email,)
	cursor.execute('SELECT * FROM user WHERE email=?', values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid Credentials")
	return row
