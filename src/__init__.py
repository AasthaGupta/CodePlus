# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-04-09 17:23:01

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
    	userdata = session['user']
    	username = session['user']['username']
    	subData = functions.getQuestions(username)
    	subData2 = functions.getSubmissions(username)
    	return render_template('student-dashboard.html', userdata=userdata, subData = subData, subData2 = subData2)
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
		userdata=session['user']
		username=session['user']['username']
		status=None
		error=None
		msg=None
		subData = functions.getQuestions(username)
		if request.method == 'POST':
			result=request.form
			status=functions.submission(result,username)
			if status['success'] == True :
				msg = "Solution saved!"
			else:
				error = "Error: " + status['error']
		return render_template('submission.html',message=msg,error=error,userdata=userdata,subData=subData)
	else:
		return render_template('404.html'),404

@app.route('/dashboard/question/', methods=['POST','GET'])
def question():
	if 'email' in session:
		userdata=session['user']
		username = session['user']['username']
		status=None
		error=None
		msg=None
		if request.method == 'POST':
			result=request.form
			status=functions.question(result,username)
			if status['success'] == True :
				msg = "Question added successfully!!"
			else:
				error = "Error: " + status['error']
		return render_template('question.html',message=msg, error=error, userdata=userdata)
	else:
		return render_template('404.html'),404

@app.route('/dashboard/deleteAccount/', methods=['POST','GET'])
def delete():
	if 'email' in session:
		if request.method == 'POST':
			username = session['user']['username']
			oid = session['user']['o_id']
			status=functions.deleteAccount(username,oid)
			if status['success'] == True :
				msg="Account Deleted!!"
				session.pop('email', None)
				session.pop('user', None)
				return  redirect(url_for('index',message=msg))
			else:
				userdata=session['user']
				error="Error:" + status['error']
				return render_template('delete-account.html',error=error,userdata=userdata)
		else:
			userdata=session['user']
			return render_template('delete-account.html',userdata=userdata)
	else:
		return redirect(url_for('index',message="Please login!"))



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
