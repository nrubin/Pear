Pear
===============

For those that want more than dinner


Setup
----------------------
###Dependencies
This package has the following non-pip dependencies:
+ postgresql
+ psycog2

###Environment Variables
+ SQLALCHEMY_DATABASE_URI - should contain the database URI
+ PEAR_ENV - should contain 'PROD', 'TEST', or 'DEV' (default is 'DEV')

###Running the app
Execute the following in the terminal from the root directory
```
python run.py
```