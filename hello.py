from Flask import flask
app=Flask(__name__)

@app.route('/')
def index():
	return 'index page  welcome'

