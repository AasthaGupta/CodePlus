# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-03-30 21:01:53

from flask import Flask ,render_template,session,request,redirect,url_for
app = Flask(__name__)

from util import assets,database

@app.route('/')
@app.route('/index')
def index():
	if 'logged' in session:
		return redirect(url_for('dashboard'))
	return  render_template('guest-login.html')

@app.route('/signup/')
def signup():
	return render_template('guest-signup.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		result = request.form
		session['logged'] = True
		session['user-email'] = result['user-email']
	return  redirect(url_for('dashboard'))

@app.route('/dashboard/', methods=['POST', 'GET'])
def dashboard():
	if 'logged' in session:
		return render_template('student-dashboard.html')
	else:
		return redirect(url_for('index'))

@app.route('/logout/')
def logout():
	if 'logged' in session:
		session.pop('user-email', None)
		session.pop('logged', None)
		session.pop('username', None)
	return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
	return render_template('error.html'), 404

database.sql_init()

if __name__ == '__main__':
	app.run(debug=True)