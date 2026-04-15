#################################################################
# Python Lib Imports

from subprocess import run
from json import loads
from byteformatter import get_size


#################################################################
# Local Imports

from .args import UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP
from .args import video_metadata_args, audio_metadata_args, video_download_args, audio_download_args


#################################################################
# Constants

METADATA_KEYS = (
    'uploader',
    'title',
    'duration_string',
    'thumbnail',
    'original_url'
)

FILE_INFO = (
    'format_id',
    'filesize_approx',
    'resolution',
    'fps',
    'vcodec',
    'acodec',
)


#################################################################
# Process Command Functions

def update_dlp_environment():
    for args in (UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP):
        result = run(args, capture_output=True, text=True)

        if result.returncode:
            raise RuntimeError(result.stderr)
        

def get_raw_json(url: str, excludeVideo: bool):
    args: tuple = None
    
    if excludeVideo:
        args = audio_metadata_args(url)

    else:
        args = video_metadata_args(url)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    
    rawJson: dict = loads(result.stdout)

    return rawJson


def get_link_metadata(url: str, excludeVideo: bool) -> dict:
    
    args: tuple = None
    
    if excludeVideo:
        args = audio_metadata_args(url)

    else:
        args = video_metadata_args(url)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    
    rawJson = loads(result.stdout)

    mediaInfo = {k: rawJson[k] for k in METADATA_KEYS}

    fileInfo = {k: rawJson[k] for k in FILE_INFO}

    mediaInfo['type'] = 'audio' if excludeVideo else 'video'

    fileInfo['filesize_approx'] = get_size(fileInfo['filesize_approx'])

    return mediaInfo | fileInfo


def download_media_file(url: str, formatIds: str, directory: str, filename: str, excludeVideo: bool):

    args: tuple = None
    
    if excludeVideo:
        args = audio_download_args(url, formatIds, filename)

    else:
        args = video_download_args(url, formatIds, filename)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
