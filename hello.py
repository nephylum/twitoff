"""Minimal flask app"""

from flask import flask
#make the application

app = Flask(__name__)

#make the route
@app.route("/")

#Now define a function
def hello:
    return "Hello World!"
