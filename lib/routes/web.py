#################################################################
# Python Lib Imports

from flask import Blueprint, render_template, request


#################################################################
# Blueprint Object

# web related blueprint
web_bp = Blueprint('web', __name__)


#################################################################
# Web Routes

@web_bp.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')




