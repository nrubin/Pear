import requests
from flask import abort, request, current_app
import hashlib, hmac
from .. import app
    
def genSecrets():
    access_token = request.args.get('access_token')
    app_secret = current_app.config['FB_APP_SECRET']
    appsecret_proof = hmac.new(app_secret, access_token, hashlib.sha256).hexdigest()
    return access_token, appsecret_proof

def fbRequest(userid='me', edgename=None, fields=None, limit=None):
    '''
    The function that all Facebook requests should go through. Takes in 
    '''

    # get the auth secrets
    access_token, appsecret_proof = genSecrets()
    
    # build the url
    fb_url = ['https://graph.facebook.com','v2.2',userid]
    if edgename:
        fb_url.append(edgename)
    fb_url = '/'.join(fb_url)
    
    # define the query parameters
    params = {}
    params['access_token'] = access_token
    params['appsecret_proof'] = appsecret_proof
    if fields:
        params['fields'] = ','.join(fields)
    if limit:
        params['limit'] = limit

    r = requests.get(fb_url,params=params)
    data = r.json()
    
    #check for errors in the response
    if 'error' in data:
        handle_error(data['error'])
    
    return data

def handle_error(e):
    app.logger.error('FBRequest Error {code}: {type}, {message}'.format(**e))
    
    # 2500  -> No access token provided
    # 190   -> Invalid access token
    if e['code'] in [2500, 190]:
        abort(401)

def isAuthenticated():
    """
    Sends a lightweight Facebook request to check if the user has logged in
    """
    return 'id' in fbRequest(fields=['id'])

def authenticate(func):
    """
    A decorator to ensure that the user is authenticated
    before executing the function.

    This decorator should only be used if a function does not already make a Facebook call
    """
    def f(*args,**kwargs):
        if isAuthenticated():
            return func(*args,**kwargs) 
        abort(401)
    return f