from . import app
from controllers import *
from models import *
from flask import render_template, jsonify, request
from fb import authenticate

# authentication
@app.route('/auth-status/')
@authenticate
def auth():
    return jsonify({'authenticated':True})

# # user routes
# @app.route('/user/create/')
# def createUser():
#     UserController.createUser()