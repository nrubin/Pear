from . import app

@app.route('/index/')
def index():
	return 'Hello'