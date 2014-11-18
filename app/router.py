from . import app
from controllers import *
from models import *
from flask import render_template, jsonify, request
from fb import authenticate

@app.route('/api/auth-status/')
@authenticate
def user():
    return jsonify({'authenticated':True})

@app.route('/api/activities/get')
def activity():
	return ActivityController.getActivityById(activity_id)