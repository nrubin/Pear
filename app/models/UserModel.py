from .. import db
from sqlalchemy.dialects.postgresql import ARRAY

class User(db.Model):
    __tablename__ =  'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    fbid = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.Text())
    gender = db.Column(db.String(20))
    relationship_status = db.Column(db.String(20))
    interested_in = db.Column(ARRAY(db.String(20)))
    last_short_token = db.Column(db.String(250))
    last_long_token = db.Column(db.String(250))

    def __init__(self, data):
        valid_fields = ['fbid','first_name', 'last_name', 'bio', 'photo_ids',
                        'gender', 'short_access_token', 'long_access_token']
        for f in valid_fields:
            self.__dict__[f] = data.get(f,None)

    def __repr__(self):
        return '<User {first_name} {last_name}: {fbid}>'.format(**self.__dict__)