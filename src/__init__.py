# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-04-02 12:28:22

from flask import Flask ,render_template,session,request,redirect,url_for
app = Flask(__name__)
app.secret_key = 'fghCXsdRETYulko'

from util import assets ,database,functions

@app.route('/')
@app.route('/index') #entry page for the website
def index():
	if 'email' in session:
		#email = session['email']
		#print "You are already logged in as %s" %email
		return redirect(url_for('.dashboard'))
	error = request.args.get('error')
	return render_template('guest-login.html',error=error)

@app.route('/signup/')
def signup():
	error = request.args.get('error')
	return render_template('guest-signup.html',error=error)

@app.route('/register/', methods=['POST'])
def register():
	if request.method == 'POST':
		result=request.form
		status=functions.register(result)
		if status['success']== True :
			error="Registered Successfully!! Please login."
			return  redirect(url_for('index',error=error))
		else:
			error= "Error: " + status['error']
			return redirect(url_for('signup',error=error))

@app.route('/login/', methods=['POST'])
def login():
	status = None
	error = None
	if request.method == 'POST':
		result=request.form
		status=functions.login(result)
		if status['success']==True:
			session['email'] = request.form['email']
			return redirect(url_for('.dashboard'))
		error="Error: "+status['error']
	return redirect(url_for('.index',error=error))



@app.route('/dashboard/', methods=['POST', 'GET'])
def dashboard():
	if 'email' in session:
		email=session['email']
		userdata=functions.userInfo(email)
	else:
		return render_template('404.html'),404
	return render_template('student-dashboard.html',userdata=userdata)

@app.route('/logout/')
def logout():
	if 'email' in session:
		session.pop('email', None)
	return redirect(url_for('.index',error=None))

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'),404

database.sql_init()

if __name__ == '__main__':
	app.run(debug=True)