#each test suite should import its own copy of unittest and the app

import unittest
from app import app, config
import datetime
from fb_test_user import temporary_fb_user


class FBRequestTestCase(unittest.TestCase):

    def setUp(self):
        #This function is run before every test
        app.config.from_object(config.get_config('TEST'))
        self.app = app.test_client()

    @temporary_fb_user
    def test_get_initial_data(self, user_data=None):
        user_id = user_data['id']
        access_token = user_data['access_token']
        login_url = user_data['login_url']
        email = user_data['email']
        password = user_data['password']

if __name__ == '__main__':
    unittest.main()