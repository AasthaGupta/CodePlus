# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-04-04 02:57:01

from flask import Flask ,render_template,session,request,redirect,url_for
app = Flask(__name__)
app.secret_key = 'fghCXsdRETYulko'

from util import assets ,database,functions

@app.route('/')
@app.route('/index', methods=['POST','GET']) #entry page for the website
def index():
	if request.method == 'POST':
		status=None
		userdata=None
		result=request.form
		status,userdata=functions.login(result)
		if status['success']==True:
			session['email'] = request.form['email']
			return render_template('student-dashboard.html',userdata=userdata)
		msg = "Error: " + status['error']
	else:
		msg = request.args.get('message', None)

	if 'email' in session :
		return redirect(url_for('.dashboard'))

	return render_template('index.html',message=msg)

@app.route('/signup/', methods=['POST','GET'])
def signup():
	error=None
	if request.method == 'POST':
		result=request.form
		status=functions.register(result)
		if status['success']== True :
			msg="Registered Successfully!! Please login."
			return  redirect(url_for('index',message=msg))
		else:
			error= "Error: " + status['error']

	return render_template('signup.html',error=error)


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