Pear
===============

For those that want more than dinner


Setup
----------------------
###Dependencies
This package has the following non-pip dependencies:
+ postgresql
+ python-dev
+ libpq-dev
+ Heroku toolbelt

Install them with apt:
```
sudo apt-get install postgresql libpq-dev python-dev && wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

###Environment Variables
+ DATABASE_URL - should contain the database URL
+ PEAR_ENV - should contain 'PROD', 'TEST', or 'DEV' (defaults to 'DEV' if unset)

###Local Database Setup
1. Add yourself as a superuser to postgres:
```sudo -u postgres createuser --superuser $USER```
2. Login to the default database with superuser permissions:
```sudo -u postgres psql```
3. Add a password for the new user:
```\password <username>```
4. Exit the postgres shell:
```\q ```
5. Add the pear_dev database under your new username:
```sudo -u $USER createdb pear_dev``` 
6. Add make sure the following command is executed each time you open a new shell or run this project (.bashrc)
```export DATABASE_URL="postgresql://<username>:<password>@localhost/pear_dev"```

Running the app
-------------------
Execute the following in the terminal from the root directory
```
foreman start
```

Database Migrations
-----------------------
###Local Database Migrations

When defining a new migration, generate the migration file in \migrations\versions and populate it automatically with 
```python manage.py db migrate```
or setup the migration file manually with
```python manage.py db revision```

Finally apply the migration to the database with
```python manage.py db upgrade```

###Remote Database Migration
Because the migration files will be generated and tested locally, applying the migration to the production database just involves the upgrade step
```heroku run python manage.py db upgrade --app <app_name>```
where ```<app_name>``` is the name of the app that you are migrating the db for

Heroku Remotes
----------
Dev: Pear
git@github.com:nrubin/Pear.git

Production: pear-app
git@heroku.com:pear-app.git

Staging: pear-stg
git@heroku.com:pear-stg.git
