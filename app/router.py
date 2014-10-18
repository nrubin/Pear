from . import app
from controllers import *

@app.route('/')
@app.route('/index/')
def index():
	return 'Hello'

