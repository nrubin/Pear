import requests
from app import app, config

def getAppAccessToken():
    fb_url = 'https://graph.facebook.com' + \
                '/oauth' + \
                '/access_token'
    params = {
        'client_id':app.config['FB_APP_ID'],
        'client_secret':app.config['FB_APP_SECRET'],
        'grant_type':'client_credentials'
    }
    resp = requests.get(fb_url, params=params)
    return resp.text.split('=')[1]

def createFBTestUser(app_access_token):
    """
    Creates a Facebook test user for an app with a random name
    Returns a dictionary with relevant data:
        -id
        -access_token
        -login_url
        -email
        -password
    """
    fb_url = 'https://graph.facebook.com' + \
                '/v2.2' + \
                '/{app_id}'.format(app_id = app.config['FB_APP_ID']) + \
                '/accounts' + \
                '/test-users'
    params = {
                'installed':'true',
                'permissions':','.join(app.config['FB_APP_PERMISSIONS']),
                'access_token':app_access_token
             }
    resp = requests.post(fb_url, params=params)
    data = resp.json()

    assert 'error' not in data

    return data

def deleteFBTestUser(app_access_token, user_id):
    """
    Deletes a Facebook test user
    """
    fb_url = 'https://graph.facebook.com' + \
                '/v2.2' + \
                '/{user_id}'.format(user_id = user_id)
    params = {
        'access_token':app_access_token
    }
    resp = requests.delete(fb_url, params=params)
    data = resp.json()
    print data
    assert data.get('success',False)

def temporary_fb_user(func):
    """
    A decorator that creates a test user, passes it to
    the function in the user_data keyword argument and
    deletes the user after the function has completed
    """
    def new_func(*args, **kwargs):
        app_access_token = getAppAccessToken()
        data = createFBTestUser(app_access_token)
        kwargs['user_data'] = data
        res = func(*args, **kwargs)
        deleteFBTestUser(app_access_token, data['id'])
        return res
    return new_func
