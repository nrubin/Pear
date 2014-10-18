Pear
===============

For those that want more than dinner


Setup
----------------------
###Dependencies
This package has the following non-pip dependencies:
+ postgresql
+ python-dev
```
sudo apt-get install postgresql python-dev
```

###Environment Variables
+ SQLALCHEMY\_DATABASE\_URI - should contain the database URI
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
```export DATABASE_URI= postgresql://<username>:<password>@localhost/pear_dev```

###Database Migrations
The first time you create the database run then following command from the root directory
```python run.py db init```
To migrate and upgrade the database run the following commands
```
python run.py db migrate
python run.py db upgrade
```

###Running the app
Execute the following in the terminal from the root directory
```
python run.py runserver
```
