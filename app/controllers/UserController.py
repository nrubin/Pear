from ..models import UserModel
from .. import fb
from .. import app


def createUser():
    """
    Controller to create a new user.
        1. Fetches initial user data 
        2. TODO: Validates profile
        3. TODO: Checks for existance in database
        4. TODO: Saves profile
        5. Returns success
    """
    user_data = fb.get_initial_user_data()
    raise NotImplementedError

def getUserById(user_id):
    """
    Returns the user object with this user_id
    """
    raise NotImplementedError

def getCurrentUser():
    """
    Returns the object representing the current user
    """
    raise NotImplementedError

def deactivateUser(user_id):
    """
    Deactivates the user with this user_id
    """
    raise NotImplementedError