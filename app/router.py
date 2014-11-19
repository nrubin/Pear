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

# activity routes
@app.route('/api/activities/get')
def activity():
    activity_id = request.args.get['activity_id']
    return ActivityController.getActivityById(activity_id)

# user routes
@app.route('/user/', methods=['GET','POST','PUT','DELETE'])
def userRoutes():
    #Note: access_token is in the url as a query parameter
    if request.method == 'GET':
        UserController.getUserById()
    elif request.method in ['POST', 'PUT']:
        # create user won't make duplicate copies of the same user, so PUT should be safe here
        UserController.createUser()
    elif request.method == 'DELETE':
        # we don't delete data, we just deactivate the account
        UserController.deactivateUser()