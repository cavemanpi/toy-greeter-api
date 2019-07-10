from functools import wraps
from flask import Flask, Response, request
import os
import json
import random

app = Flask(__name__)

VALID_USER = os.environ.get('USER', 'default')
VALID_PASSWORD = os.environ.get('PASSWORD', 'default')

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == VALID_USER and password == VALID_PASSWORD

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/")
@requires_auth
def salutation():
    
    options = ['old, chum', 'my good person', 'gentleperson', 'you old so and so']
    return json.dumps({
        'salutation': random.choice(options),
    })

@app.route("/status")
def status():
    return "OK"
