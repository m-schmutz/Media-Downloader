from .paths import YT_DLP_PATH, DENO_JS_PATH, YT_DLP_PIP_PATH, YT_DLP_PY_PATH
from subprocess import run

from json import loads




# arguments

def _metadata_args(videoUrl: str) -> list[str]:
    return [
        'env/bin/python3',
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-J',
        videoUrl
    ]



# yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" <VIDEO_URL>


def _video_download_args(videoUrl: str, filename: str):
    return [
        'env/bin/python3',
        YT_DLP_PATH,
        '--js-runtimes',
        f'deno:{DENO_JS_PATH}',
        '-f',
        'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        '-o',
        filename,
        videoUrl
    ]



def _audio_download_args():
    pass



def update_yt_dlp():
    args = [YT_DLP_PIP_PATH, 'install', '-U', 'yt-dlp-ejs']
    args2 = [YT_DLP_PY_PATH, YT_DLP_PATH, '-U']





def get_video_metadata(videoUrl: str):

    args = _metadata_args(videoUrl)

    result = run(args, capture_output=True, text=True)

    if result.returncode:
        raise RuntimeError(result.stderr)

    metadata = loads(result.stdout)

    return (
        metadata['title'],
        metadata['channel'],
        metadata['thumbnail'],
        metadata['uploader_url'],
        metadata['original_url'],
        metadata['duration_string']
    )

def download_video(videoUrl: str, filename: str):
    args = _video_download_args(videoUrl, filename)

    result = run(args)
