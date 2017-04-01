from . import database

def login(form):
	status = { 'success' : True }
	try:
		email = form['email']
		password = form['password']
		row = database.get_user(email,password)
		userdata=None
		#use row data to populate userdata
	except Exception as e:
		status['error'] = str(e)
		status['success'] = False
	return status,userdata


def register(form):
	status = {'success' : True}
	try:
		name=form['name']
		username=form['username']
		password=form['password']
		password2=form['password2']
		email=form['email']
		#add rest of the fields

		if password != password2:
			raise ValueError('Password does not match')

		if database.username_exist(username):
			raise ValueError('Username already taken')

		if database.email_exist(email):
			raise ValueError('email already registered')

		database.add(name,email,username,password)
		#add rest of the columns

	except Exception as e:
		status['error'] = str(e)
		status['success'] = False
	return status