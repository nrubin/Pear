#each test suite should import its own copy of unittest and the app

import unittest
import app
import datetime

import json

class ActivityTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.app.test_client()

	def test_add_activity(self):
		rv = self.app.post('/api/activities/add',data=dict(name='DummyActivity',description='A Dummy Activity'),follow_redirects=True)
		assert "DummyActivity" in rv.data

	def test_add_big_activity(self):
		name = "A Big Activity"
		description = "A large activity with a large description, mostly describing useless things but just in case we will make it super large. Hello world, lorem ipsum dolor sit amet, yes I did just write that from memory. You know what? <strong> Lets </strong> write some <p> html too! </p>"
		duration = 60 * 60 * 1000 #AKA an hour
		difficulty = "EASY"
		pricing = json.dumps({"1 lesson":55,"5 lessons":300})
		photos = ["http://i.imgur.com/43ddDwa.jpg","http://i.imgur.com/43ddDwa.jpg"]
		schedule = [datetime.datetime.now(),datetime.datetime.now()]

		bigActivity = dict(name=name,description=description,duration=duration,difficulty=difficulty,pricing=pricing,photos=photos,schedule=schedule)

		rv = self.app.post('/api/activities/add',data=bigActivity)
		assert "Big Activity" in rv.data

	def test_get_activity(self):
		rv = self.app.get('/api/activities/get',data=dict(name="DummyActivity"))
		assert "DummyActivity" in rv.data

