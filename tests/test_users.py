import unittest
from app import app, config
import datetime

class UserTestCase(unittest.TestCase):

    def setUp(self):
        #This function is run before every test
        app.config.from_object(config.get_config('TEST'))
        self.app = app.test_client()

    def test_create_user(self):
        