# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-03-31 14:35:26



from flask import Flask ,render_template,session,request,redirect,url_for
app = Flask(__name__)

from util import assets ,database,functions

@app.route('/')
@app.route('/index') #entry page for the website
def index():
	return render_template('guest-login.html')

@app.route('/signup/')
def signup():
	return render_template('guest-signup.html')

@app.route('/register/', methods=['POST'])
def register():
	if request.method == 'POST':
		result=request.form
		status=functions.register(result)
		if status['success']== True :
			return  redirect(url_for('index'))
		else:
			return redirect(url_for('signup'))

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		result=request.form
		status=functions.login(result)
		if status['success']==True:
			return render_template('student-dashboard.html')
	return  redirect(url_for('index'))

@app.route('/dashboard/', methods=['POST', 'GET'])
def dashboard():
	return render_template('student-dashboard.html')

@app.route('/logout/')
def logout():
	if 'logged' in session:
		session.pop('user-email', None)
		session.pop('logged', None)
		session.pop('username', None)
	return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'),404

database.sql_init()

if __name__ == '__main__':
	app.run(debug=True)