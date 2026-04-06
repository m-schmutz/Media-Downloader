#!./web-env/bin/python3

# from lib.ytdlp import update_dlp_environment, get_link_metadata, download_media_file
# from lib.ytdlp.args import audio_download_args


# smittyVideo = 'https://youtu.be/u8sRY0tKTuc?si=XsVdOj9-vLfPAoFq'

# githubUrl = 'https://github.com/yt-dlp/yt-dlp'

# exclude = False

# directory = '/home/msch/Projects/Media-Downloader/downloads'

# try: 
#     get_link_metadata(githubUrl, False)

# except Exception as e:
#     print(e)

from uuid import uuid4


HEX_DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

def _check_valid_uuid(uuid: str):
    if len(uuid) != 32:
        raise ValueError('uuid is not valid length')
    
    for digit in uuid:
        if digit not in HEX_DIGITS:
            raise ValueError(f'{digit} is not a valid uuid character')






