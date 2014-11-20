from . import app
from controllers import *
from models import *
from flask import render_template, jsonify, request
from fb.auth import authenticate

# authentication
@app.route('/api/auth-status/')
@authenticate
def auth():
    return jsonify({'authenticated':True})

# activity routes
@app.route('/api/activity/', methods=['GET'])
def activity():
    if request.method == 'GET':
        activity_id = request.args.get['activity_id']
        return ActivityController.getActivityById(activity_id)

# user routes
@app.route('/api/user/', methods=['GET','POST','PUT','DELETE'])
def user():
    if request.method == 'GET':
        # return the current user or another user
        user_id = request.args.get('user_id',None)
        if user_id is not None:
            return UserController.getUserById(user_id)
        return UserController.getCurrentUser()

    elif request.method in ['POST', 'PUT']:
        # create user won't make duplicate copies of the same user, so PUT should be safe here
        UserController.createUser()
    elif request.method == 'DELETE':
        # we don't delete data, we just deactivate the account
        UserController.deactivateUser()