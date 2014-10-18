Pear
===============

For those that want more than dinner


Setup
----------------------
###Dependencies
This package has the following non-pip dependencies:
+ postgresql
+ python-dev

###Environment Variables
+ SQLALCHEMY_DATABASE_URI - should contain the database URI
+ PEAR_ENV - should contain 'PROD', 'TEST', or 'DEV' (default is 'DEV')

###Local Database Setup
1. Install PostgreSQL
2. Install python-dev in order to pip install psycopg2
3. Add yourself as a superuser to postgres: sudo -u postgres createuser --superuser $USER
4.Login to the default database with superuser permissions: sudo -u postgres psql
5. Add a password for the new user: postgres=# \password <username>
6. Exit the postgres shell: \q
7. Add the pear_dev database under your new username: sudo -u $USER createdb pear_dev

You should now be able to access the postgres database with the command: psql pear_dev

With the database setup, make sure that your environment variable DATABASE_URI is set to ```postgresql://<username>:<password>@localhost/pear_dev```

###Running the app
Execute the following in the terminal from the root directory
```
python run.py
```