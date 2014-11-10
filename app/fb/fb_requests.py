from auth import fbRequest
from flask import request

def get_initial_user_data():
    """
    A request fired upon profile create to fetch a user's information
    """
    # create data dictionary and initial population
    user_data = {}
    user_data['short_access_token'] = request.args.get('access_token')
    
    # send the user data fbRequest
    core_fields = ['id','first_name','last_name','gender','birthday','email']
    opt_fields = ['relationship_status','bio','interested_in']
    fields = core_fields + opt_fields
    d = fbRequest(fields=fields)
    
    # rename id to fbid and add d to data
    user_data['fbid'] = d['id']
    d.pop('id')
    user_data.update(d)
    return user_data
    
def get_initial_photo_data():
    """
    A request fired upon profile create to fetch a user's photos
    """
    raise NotImplementedError
    # send the photos fbRequest
    photo_data = fbRequest(edgename='photos',fields=['source'],limit=5)
    return photo_data['data']