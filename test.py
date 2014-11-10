from app import app, db, config
import unittest
import os
from tests import *

if __name__ == '__main__':
	os.environ["PEAR_ENV"] = "TEST"
	unittest.main()