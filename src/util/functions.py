from . import database

def login(form):
	status = { 'success' : True }
	userdata=None
	try:
		email = form['email']
		password = form['password']
		userdata = database.get_user(email,password)
	except Exception as e:
		status['error'] = str(e)
		status['success'] = False
	return status,userdata


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

		database.add(fname,lname,email,username,password,country,dob,oname,otype,ocity,ocountry)

	except Exception as e:
		status['error'] = str(e)
		status['success'] = False

	return status