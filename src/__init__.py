# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-04-08 18:19:47

from flask import Flask ,render_template,session,request,redirect,url_for
app = Flask(__name__)
app.secret_key = 'fghCXsdRETYulko'

from util import assets, database, functions

@app.route('/')
@app.route('/index', methods=['POST','GET']) #entry page for the website
def index():
	status=None
	userdata=None
	error=None
	msg=None
	if request.method == 'POST':
		result=request.form
		status,userdata=functions.login(result)
		if status['success']==True:
			session['email'] = request.form['email']
			session['user']=userdata
		else:
			error = "Error: " + status['error']
	else:
		msg = request.args.get('message', None)

	if 'email' in session :
		return redirect(url_for('.dashboard'))

	return render_template('index.html',message=msg,error=error)

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

@app.route('/forgotPassword/', methods=['POST','GET'])
def forgotPass():
	error=None
	if request.method == 'POST':
		email=request.form['email']
		print email
		status=functions.forgotPassword(email)
		if status['success']== True :
			msg="Mail sent!!"
			return  redirect(url_for('index',message=msg))
		else:
			error= "Error: " + status['error']

	return render_template('forgot-password.html',error=error)


@app.route('/dashboard/', methods=['GET'])
def dashboard():
	if 'email' in session:
		userdata=session['user']
		return render_template('student-dashboard.html',userdata=userdata)
	else:
		return render_template('404.html'),404



@app.route('/dashboard/editAccount/', methods=['POST','GET'])
def edit():
	if 'email' in session:
		if request.method == 'POST':
			result=request.form
			status, userdata=functions.updateAccount(result)
			if status['success'] == True :
				msg="Updated successfully!!"
				session['user']=userdata
				return  render_template('student-account-edit.html',message=msg, userdata=userdata)
			else:
				return render_template('404.html'),404
		else:
			userdata=session['user']
			return render_template('student-account-edit.html',userdata=userdata)
	else:
		return redirect(url_for('index',message="Please login!"))


@app.route('/dashboard/submission/', methods=['POST','GET'])
def submission():
	if 'email' in session:
		status=None
		error=None
		msg=None
		if request.method == 'POST':
			result=request.form
			status=functions.submission(result)
			if status['success'] == True :
				msg = status['status']
			else:
				error = "Error: " + status['error']
		return render_template('submission.html',message=msg,error=error)
	else:
		return render_template('404.html'),404

@app.route('/dashboard/question/', methods=['POST','GET'])
def question():
	if 'email' in session:
		status=None
		error=None
		msg=None
		if request.method == 'POST':
			result=request.form
			status=functions.question(result)
			if status['success'] == True :
				msg = "Question added successfully!!"
			else:
				error = "Error: " + status['error']
		return render_template('question.html',message=msg, error=error)
	else:
		return render_template('404.html'),404


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
