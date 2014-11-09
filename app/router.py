from . import app
from controllers import *
from models import *
from flask import render_template, jsonify, request
from fb import authenticate

@app.route('/auth-status/')
@authenticate
def user():
    return jsonify({'authenticated':True})