#################################################################
# Local Imports

from ..config import DLP_ENV_PIP, DLP_ENV_PY, YT_DLP_PATH, DENO_JS_PATH


#################################################################
# Static Arguments

UPDATE_DLP_PIP = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'pip'
)


UPDATE_DLP_EJS = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'yt-dlp-ejs'
)


UPDATE_YT_DLP = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '-U'
)


#################################################################
# Dynamic Arguments

def video_metadata_args(url: str):
    return (
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '--no-playlist',
        '-J',
        '-f',
        'bv*+ba/b',
        url
    )


def audio_metadata_args(url: str):
    return (
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '--no-playlist',
        '-J',
        '-f',
        'ba/bestaudio',
        url
    )


def video_download_args(url: str, formatIds: str, directory: str, filename:str):
    return (
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-f',
        formatIds,
        '--merge-output-format',
        'mp4',
        '-o',
        f'{directory}/{filename}.mp4',
        url
    )


def audio_download_args(url: str, formatIds: str, directory: str, filename:str):
    return (
        DLP_ENV_PY,
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-f',
        formatIds,
        '--audio-format',
        'mp3',
        '-o',
        f'{directory}/{filename}.mp3',
        url
    )
