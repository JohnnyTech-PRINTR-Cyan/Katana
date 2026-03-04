import flask
from flask import *
from version import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', version=v)
