#each test suite should import its own copy of unittest and the app

import unittest
import app
class ActivityTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.app.test_client()

	def test_add_activity(self):
		rv = self.app.post('/api/activities/add',data=dict(name='DummyActivity',description='A Dummy Activity'),follow_redirects=True)
		assert "DummyActivity" in rv

	def test_get_activity(self):
		rv = self.app.get('/api/activities/get',data=dict(name="DummyActivity"))
		assert "DummyActivity" in rv