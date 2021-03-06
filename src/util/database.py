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

def link_exists(link, username):
	if link is "" :
		return True
	connection = sql_connect()
	cursor = connection.cursor()
	values=(username, link,)
	cursor.execute('SELECT * FROM adds NATURAL JOIN question WHERE username = ? and link = ?', values)
	return cursor.fetchone() is not None

def updateUser(fname,lname,email,username,country,dob,oid,oname,otype,ocity,ocountry):
	connection = sql_connect()
	cursor = connection.cursor()

	userInfo = (fname,lname,country,dob,email,)
	orgInfo = (oname,otype,ocity,ocountry,oid,)
	print userInfo
	sql1 = "UPDATE user SET fname = ?, lname = ?, country = ?, dob = ? WHERE email = ? "
	sql2 = "UPDATE organisation SET oname = ?, otype = ?, ocity = ?, ocountry = ? WHERE o_id = ? "

	cursor.execute(sql1, userInfo)
	print "added into table user"
	cursor.execute(sql2, orgInfo)
	print "added into table organisation"
	connection.commit()
	print "user info updated"

def addSubmission(q_code, q_name, language, s_time, s_date, status, username):
	connection = sql_connect()
	cursor = connection.cursor()
	subInfo = (s_date, s_time, language, status,)
	cursor.execute("INSERT INTO solution ( s_date, s_time, language, status ) VALUES (?,?,?,?)", subInfo)
	connection.commit()
	cursor.execute("SELECT * FROM solution WHERE s_date = ? and s_time = ? and language = ? and status = ?", subInfo)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("No submission added")
	s_id = row[0]
	cursor.execute("INSERT INTO submits (s_id, username) VALUES (?,?)", (s_id, username,))
	cursor.execute("INSERT INTO solution_of (s_id, q_code) VALUES (?,?)", (s_id, q_code,))
	connection.commit()
	print "submission added"

def addQuestion(q_name, difficulty, link, username):
	connection = sql_connect()
	cursor = connection.cursor()
	quesInfo = (q_name, difficulty, link)
	print quesInfo
	cursor.execute("INSERT INTO question (q_name, difficulty, link ) VALUES (?,?,?)", quesInfo)
	connection.commit()
	cursor.execute('SELECT * FROM question WHERE q_name = ? and difficulty = ? and link = ?', quesInfo)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("No question added")
	q_code = row[0]
	cursor.execute("INSERT INTO adds (username,q_code) VALUES (?,?)",(username,q_code,))
	connection.commit()
	print "question added"

def get_oid(username):

	connection = sql_connect()
	cursor = connection.cursor()
	values = (username,)
	cursor.execute("SELECT o_id FROM member_of WHERE username=?",values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid username")
	return row[0]

def deleteUser(username,oid):
	connection = sql_connect()
	cursor = connection.cursor()
	cursor.execute("DELETE FROM user WHERE username = ?",(username,))
	print "Record deleted from user table"
	cursor.execute("DELETE FROM member_of WHERE o_id =?",(oid,))
	print "Record deleted from member_of table"



def get_user(email, password):
	connection = sql_connect()
	cursor = connection.cursor()
	values = (email,password,)
	cursor.execute('SELECT * FROM user WHERE email=? and password=?', values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid Credentials")
	return row

def getQuestions(username):
    connection = sql_connect()
    cursor = connection.cursor()
    values=(username,)
    cursor.execute('SELECT q_name, difficulty, link, q_code FROM adds NATURAL JOIN question WHERE username=?', values)
    rows = cursor.fetchall()
    return rows

def getSubmissions(username):
    connection = sql_connect()
    cursor = connection.cursor()
    values = (username,)
    cursor.execute('SELECT q_name,status,s_date,s_time,language FROM submits NATURAL JOIN solution_of NATURAL JOIN solution NATURAL JOIN question WHERE username=?', values)
    rows = cursor.fetchall()
    return rows


def get_user_organisation(o_id):
	connection = sql_connect()
	cursor = connection.cursor()
	values = (o_id,)
	cursor.execute('SELECT * FROM organisation WHERE o_id =?', values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid oid")
	return row

def get_user_by_email(email):
	connection = sql_connect()
	cursor = connection.cursor()
	values = (email,)
	cursor.execute('SELECT * FROM user WHERE email=?', values)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("Invalid email")
	return row

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
	cursor.execute('SELECT * FROM organisation WHERE oname = ? and otype = ? and ocity = ? and ocountry = ?', orgInfo)
	row = cursor.fetchone()
	if row is None:
		raise ValueError("No organisation found")
	oid = row[0]
	cursor.execute("INSERT INTO member_of (username,o_id) VALUES (?,?)",(username,oid,))
	connection.commit()
	print "user added"
