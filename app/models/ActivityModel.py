from .. import db
from sqlalchemy.dialects.postgresql import JSON as psql_json #pricing is iffy, so let's just store it as json
from sqlalchemy.dialects.postgresql import ARRAY as psql_array

class Activity(db.Model):
    __tablename__ =  'activites'
    
    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    duration = db.Column(db.BigInteger) #duration of activity in ms
    difficulty = db.Column(db.String(80))
    pricing = db.Column(psql_json)
    schedule = db.Column(psql_array(db.DateTime(timezone=False)))

    def __init__(self, name, description, duration=None, difficulty=None, pricing=None, photos=None, schedule=None):
        self.name = name
        self.description = description

        if duration is not None:
            self.duration = duration
        if difficulty is not None:
            self.difficulty = difficulty
        if pricing is not None:
            self.pricing = pricing
        if photos is not None:
            self.photos = photos
        if schedule is not None:
            self.schedule = schedule

    def __repr__(self):
        return '<Activity %r>' % self.name