import os

class Config(object):
	"""
	Basic configuration parameters for any environment
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	FB_APP_SECRET = os.environ.get('FB_APP_SECRET')
	FB_APP_ID = os.environ.get('FB_APP_ID')
	FB_APP_PERMISSIONS = ['public_profile','email','user_friends']

class ProductionConfig(Config):
	"""
	Configuration parameters specific to production
	"""
	pass

class TestingConfig(Config):
	"""
	Configuration parameters specific to the testing environment
	"""
	TESTING = True

class DevelopmentConfig(Config):
	"""
	Configuration parameters specific to the development environment
	"""
	DEBUG = True

def get_config(env=None):
	"""
	Returns an object representation of the app config
	"""
	# if the env argument is specified it should overwrite the os environment variable
	env = env or os.environ.get('PEAR_ENV')
	if env == 'PROD':
		return ProductionConfig
	elif env == 'TEST':
		return TestingConfig
	else:
		return DevelopmentConfig