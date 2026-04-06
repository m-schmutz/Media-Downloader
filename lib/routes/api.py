#################################################################
# Python Lib Imports

from flask import Blueprint, jsonify, request


#################################################################
# Local Imports

from ..ytdlp import get_link_metadata


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

        if not mediaUrl or not mediaType:
            return jsonify({'error': 'Missing required fields: url, type'}), 400

        excludeVideo = (mediaType == 'audio')

        metadata = get_link_metadata(mediaUrl, excludeVideo)

        return jsonify({'file-info': metadata}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500