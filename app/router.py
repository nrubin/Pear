from . import app
# from controllers import *
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')