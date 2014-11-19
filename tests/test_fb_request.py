#each test suite should import its own copy of unittest and the app

import unittest
from app import app, config, fb
import datetime
from fb_test_user import temporaryFBUser
import json

class FBRequestTestCase(unittest.TestCase):

    def setUp(self):
        #This function is run before every test
        app.config.from_object(config.get_config('TEST'))
        self.app = app.test_client()

    @temporaryFBUser
    def test_get_initial_data(self, user_data=None):
        with app.test_request_context('/?access_token={access_token}'.format(access_token=user_data['access_token'])):
            resp_data = fb.get_initial_user_data()
            print resp_data
            assert resp_data['fbid'] == user_data['id']
            assert resp_data['short_access_token'] == user_data['access_token']
            assert resp_data['email'] == user_data['email']
            assert 'first_name' in resp_data
            assert 'last_name' in resp_data
            assert 'gender' in resp_data
            assert 'birthday' in resp_data

    def test_get_initial_photo_data():
        pass
