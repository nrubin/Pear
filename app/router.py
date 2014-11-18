from . import app
from controllers import *
from models import *
from flask import render_template, jsonify, request
from fb import authenticate

# authentication
@app.route('/api/auth-status/')
@authenticate
def auth():
    return jsonify({'authenticated':True})

@app.route('/api/activities/get')
def activity():
    return ActivityController.getActivityById(activity_id)

# # user routes
# @app.route('/user/create/')
# def createUser():
#     UserController.createUser()