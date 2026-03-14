## Basic skeleton for a flask project
from flask import Flask

##WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to this flask course, and am hoping your life will change for the best'


@app.route('/index')
def index():
    return 'This is the index page'



if __name__=='__main__':
    app.run(debug=True)


