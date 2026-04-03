
from .paths import DLP_ENV_PY, DLP_ENV_PIP, YT_DLP_PATH, DENO_JS_PATH
from subprocess import run
from json import loads



UPDATE_PIP = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'pip'
)


UPDATE_EJS = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'yt-dlp-ejs'
)


UPDATE_DLP = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '-U'
)



VIDEO_METADATA = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '--js-runtimes',
    f'deno:{DENO_JS_PATH}',
    '-J'
)


VIDEO_DOWNLOAD = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '--js-runtimes',
    f'deno:{DENO_JS_PATH}',
    '-f',
    'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
    '-o',
)

AUDIO_DOWNLOAD = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '--js-runtimes',
    f'deno:{DENO_JS_PATH}',
    '-f',
    'bestaudio',
    '--extract-audio',
    '--audio-format',
    'mp3',
    '--audio-quality',
    '0',
    '-o'
)


def update_dlp_environment():
    
    for args in [UPDATE_PIP, UPDATE_DLP, UPDATE_EJS]:
        result = run(args, capture_output=True, text=True)

        if result.returncode:
            raise RuntimeError(result.stderr)
        

def get_video_metadata(videoUrl: str):
    
    args = VIDEO_METADATA + (videoUrl,)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    
    metadata = loads(result.stdout)


    return (
        metadata['title'],
        metadata['channel'],
        metadata['thumbnail'],
        metadata['webpage_url'],
        metadata['duration_string']
    )


def download_video(videoUrl: str, filename: str):

    args = VIDEO_DOWNLOAD + (filename, videoUrl)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)
    

def download_audio(videoUrl: str, filename: str):
    args = AUDIO_DOWNLOAD + (filename, videoUrl)

    print(f'{args}')

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)