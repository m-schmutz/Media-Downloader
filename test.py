#!./web-env/bin/python3

from lib.ytdlp import update_dlp_environment, get_link_metadata, get_raw_json
from lib.ytdlp.args import audio_download_args

from json import dumps



smittyVideo = 'https://youtu.be/u8sRY0tKTuc?si=XsVdOj9-vLfPAoFq'

# githubUrl = 'https://github.com/yt-dlp/yt-dlp'


rawVideoJsonPath = '/home/msch/Projects/Media-Downloader/json-stuff/video-raw-meta.json'

rawAudioJsonPath = '/home/msch/Projects/Media-Downloader/json-stuff/audio-raw-meta.json'


rawVideoMeta = get_raw_json(smittyVideo, False)

rawAudioMeta = get_raw_json(smittyVideo, True)



with open(rawVideoJsonPath, 'w') as f:
    f.write(dumps(rawVideoMeta))



with open(rawAudioJsonPath, 'w') as f:
    f.write(dumps(rawAudioMeta))