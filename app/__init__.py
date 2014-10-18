# This file contains sets up the app object and
# sets up all of the extensions

import os
import config
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

# Create and configure app object
app = Flask(__name__)
app.config.from_object(config.get_config())

# Setup Flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)