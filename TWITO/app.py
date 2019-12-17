"""code for the app"""

from flask import Flask
from.models import DB
#make an app factory

def create_app():
    app = Flask(__name__)

    #add config for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #have the database know the about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!!'
    return app
