#################################################################
# Python Lib Imports

from flask import Blueprint, render_template, request


#################################################################
# Local Imports

from ..utils.string_utils import check_valid_uuid


#################################################################
# Blueprint Object

# web related blueprint
web_bp = Blueprint('web', __name__)


#################################################################
# Web Routes

@web_bp.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')


@web_bp.route('/new-download/<string:uuid>')
def new_download_page(uuid:str):
    pass

