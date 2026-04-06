#################################################################
# Python Lib Imports 

from flask import Flask
from sys import exit


#################################################################
# Local Imports 

from .routes import api_bp, web_bp


#################################################################
# create_app function

def create_app() -> Flask:
    # create Flask app object
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
    )

    # register blueprints
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # return Flask app object
    return app