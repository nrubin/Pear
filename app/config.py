#TODO setup the database connection
#TODO add the prod environment variable on the production machine

import os

class Config(object):
	"""
	Basic configuration parameters for any environment
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

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

def get_config():
	env = os.environ.get('PEAR_ENV')
	if env == 'PROD':
		return ProductionConfig
	elif env == 'TEST':
		return TestingConfig
	else:
		return DevelopmentConfig