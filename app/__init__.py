# This file contains sets up the app object and
# sets up all of the extensions

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask(__name__)

#TODO setup the database connection
#TODO add the prod environment variable on the production machine
if os.environ.get('PROD'):
	app.config['TEST'] = False
	# setup prod database variables
else:
	app.config['TEST'] = True
	#TODO add a database and actually populate this environment variable
	app.config['SQLALCHEMY_DAly TABASE_URI'] = os.environ.get('DATABASE_URI')
	# setup local database variabes

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

import router
manager.run()