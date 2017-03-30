# -*- coding: utf-8 -*-
# @Author: Aastha Gupta
# @Date:   2017-03-30 13:16:19
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-03-30 13:53:59

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('guest-login.html')