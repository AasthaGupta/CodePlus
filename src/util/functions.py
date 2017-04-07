from . import database
from datetime import datetime
from hashlib import md5
import random

	  	


def login(form):
	status = { 'success' : True }
	userdata=None
	try:
		email = form['email']
		password = md5(form['password']).hexdigest()
		row = database.get_user(email, password)
		email, username, password, fname, lname, country, dob = row
		o_id = database.get_o_id(username)
		row2 = database.get_user_organisation(o_id[0])
		o_id,oname,otype,ocity,ocountry = row2
		columns = ('email', 'username', 'password', 'fname', 'lname', 'country', 'dob','o_id','oname','otype','ocity','ocountry')
		userdata={}
		
		for k in columns:
			userdata[k]=eval(k)
	except Exception as e:
		status['error'] = str(e)
		status['success'] = False
	return status,userdata

def submission(form):
	status = { 'success' : True }
	try:
		q_code = form['qcode']
		language = form['language']
		s_date = datetime.now().date().strftime('%Y-%m-%d')
		s_time = datetime.now().time().strftime('%H:%M:%S')
		print s_date,s_time

		arr = ["WA","AC","TLE"]
		x = random.randrange(0,3)
		codeStatus = arr[x]
		status['status'] = codeStatus

		database.addSubmission(q_code,language,s_time,s_date,codeStatus)

	except Exception as e:
		status['error'] = str(e)
		status['success'] = False
	return status


def register(form):
	status = {'success' : True}
	try:
		fname=form['fname']
		lname=form['lname']
		email=form['email']
		username=form['username']
		password=form['password']
		password2=form['password2']
		country=form['country']
		dob=form['dob']
		oname=form['oname']
		otype=form['otype']
		ocity=form['ocity']
		ocountry=form['ocountry']
		print"taken form data"

		if database.username_exists(username):
			raise ValueError('Username already taken')

		if database.email_exists(email):
			raise ValueError('Email already registered')

		if password != password2:
			raise ValueError('Password does not match')

		password = md5(password).hexdigest()
		database.add(fname,lname,email,username,password,country,dob,oname,otype,ocity,ocountry)

	except Exception as e:
		status['error'] = str(e)
		status['success'] = False

	return status


def updateAccount(form):
	status = {'success' : True}
	try:
		oid = get_o_id(username)
		print oid
		fname=form['fname']
		lname=form['lname']
		email=form['email']
		username=form['username']
		country=form['country']
		dob=form['dob']
		oname=form['oname']
		otype=form['otype']
		ocity=form['ocity']
		ocountry=form['ocountry']
		print"taken form data"
		database.updateValue(fname,lname,email,username,country,dob,o_id,oname,otype,ocity,ocountry)

	except Exception as e:
		status['error'] = str(e)
		status['success'] = False

	return status

def userInfo(email):
	userdata = database.get_user_by_email(email)
	return userdata
