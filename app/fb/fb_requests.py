import requests
from .. import app
from flask import abort
from auth import genSecrets

def fb_request(userid='me', edgename=None, fields=None):
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

    r = requests.get(fb_url,params=params)
    data = r.json()
    
    if 'error' in data:
        pass #TODO: catch any errors from FB
    
    return data

def isAuthenticated():
    """
    Sends a lightweight Facebook request to check if the user has logged in
    """
    return 'id' in fb_request(fields=['id'])

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