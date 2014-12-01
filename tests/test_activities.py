#each test suite should import its own copy of unittest and the app

import unittest
from app import app, config, ActivityModel
from datetime import datetime
import json
import pytz

class ActivityTestCase(unittest.TestCase):

    def setUp(self):
        #This function is run before every test
        app.config.from_object(config.get_config('TEST'))
        self.app = app.test_client()

    def test_add_activity(self):
        rv = self.app.post('/api/activities/add',data=dict(name='DummyActivity',description='A Dummy Activity'),follow_redirects=True)
        assert "DummyActivity" in rv.data

    def test_add_big_activity(self):
        name = "A Big Activity"
        description = "A large activity with a large description, mostly describing useless things but just in case we will make it super large. Hello world, lorem ipsum dolor sit amet, yes I did just write that from memory. You know what? <strong> Lets </strong> write some <p> html too! </p>"
        duration = 60 * 60 * 1000 # AKA an hour
        difficulty = "EASY"
        pricing = json.dumps({"1 lesson":5500,"5 lessons":30000}) # AKA 55 dollars and 300 dollars
        photos = ["http://i.imgur.com/43ddDwa.jpg","http://i.imgur.com/43ddDwa.jpg"]
        schedule = json.dumps([datetime.datetime.now(),datetime.datetime.now()])

        bigActivity = dict(name=name,description=description,duration=duration,difficulty=difficulty,pricing=pricing,photos=photos,schedule=schedule)

        rv = self.app.post('/api/activities/add',data=bigActivity)
        assert "Big Activity" in rv.data

    def get_activity(self,name):
    	# might want to consider including the activity id as a query parameter
        return self.app.get('/api/activities/get',data=dict(name=name))

    def test_get_activity(self):
        rv = self.get_activity("DummyActivity")
        assert "DummyActivity" in rv.data

    def test_set_activity_info(self):
        activity_id = self.get_activity("DummyActivity").data["activity_id"]
        route = '/api/activities/%d' % activity_id
        rv = self.app.post(route,dict(name="NewDummyActivity"))
        assert "NewDummyActivity" in rv.data

    def test_schedule(self):
        activity = ActivityModel("Test Activity 1", "The First Test Activity")
        start_date = datetime.strptime("01/01/2014 00:01", "%m/%d/%Y %H:%M")
        end_date = datetime.strptime("01/07/2014 00:01", "%m/%d/%Y %H:%M")
        start_time = datetime.time(12,30,0,pytz.pst)
        activity.set_schedule(start_date=start_date,
                            end_date=end_date,
                            days=[2,4],
                            duration=60,
                            repeat="weekly")
        scheds = activity.get_schedules()
        assert scheds[0] = datetime.strptime("01/02/2014 00:01", "%m/%d/%Y %H:%M")