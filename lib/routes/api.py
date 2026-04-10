#################################################################
# Python Lib Imports

from flask import Blueprint, jsonify, request
from uuid import uuid4
from json import loads, dumps


#################################################################
# Local Imports

from ..ytdlp import get_link_metadata
from ..database import DBConnection, TypeValues
from ..utils.string_utils import check_valid_uuid


#################################################################
# Blueprint Object

# api related blueprint
api_bp = Blueprint('api', __name__)


#################################################################
# Api Routes


@api_bp.route('/check-link', methods=['POST'])
def check_link():
    try:
        postData: dict|None = request.get_json()

        if not postData:
           return jsonify({'error': 'No JSON data received'}), 400

        mediaUrl = postData.get('url')
        mediaType = postData.get('type')

        if not mediaUrl:
            return jsonify({'error': 'Missing required fields: url'}), 400
        
        if not mediaType:
            return jsonify({'error': 'Missing required fields: type'}), 400
        
        if mediaType not in TypeValues:
            return jsonify({'error': f'Type must be either \'{TypeValues.VIDEO}\' or \'{TypeValues.AUDIO}\''}), 400

        excludeVideo: bool = (mediaType == 'audio')

        metadata = get_link_metadata(mediaUrl, excludeVideo)

        linkUUID = uuid4().hex

        with DBConnection() as db:
            db.insert_pending(linkUUID, dumps(metadata))

        return jsonify({'uuid': linkUUID}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@api_bp.route('/pending/<string:uuid>')
def pending_download_info(uuid:str):
    try:
        issue = check_valid_uuid(uuid)

        if issue:
            return jsonify({'error': issue}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500