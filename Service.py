from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>hello world iseek.</h1>"


@app.route('/time')
def send_time():
    return {'time': time.time()}
