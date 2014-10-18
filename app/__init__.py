# This file contains sets up the app object and
# sets up all of the extensions

from flask import Flask
import os

app = Flask(__name__)

#TODO setup the database connection
#TODO add the prod environment variable on the production machine
prod = os.environ.get('PROD')
if prod:
	app.config['TEST'] = False
	# setup prod database variables
else:
	app.config['TEST'] = True
	# setup local database variables

import router
app.run()