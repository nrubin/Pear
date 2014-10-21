import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db, config

app.config.from_object(config.get_config())

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()