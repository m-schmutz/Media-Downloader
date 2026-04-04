#################################################################
# Python Lib Imports

from subprocess import run
from json import loads


#################################################################
# Local Imports

from .args import UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP, GET_LINK_JSON


#################################################################
# Internal Functions

def _extract_metadata(info: dict):
    return (
        info['uploader'],
        info['title'],
        info['duration_string'],
        info['thumbnail']
    )


#################################################################
# Process Command Functions

def update_dlp_environment():
    for args in (UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP):
        result = run(args, capture_output=True, text=True)

        if result.returncode:
            raise RuntimeError(result.stderr)


def get_link_metdata(url: str) -> dict:
    args = GET_LINK_JSON + (url,)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    
    metadataJson = loads(result.stdout)

