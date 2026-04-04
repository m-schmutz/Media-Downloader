#!/usr/bin/python3

from lib.ytdlp import update_dlp_environment, get_link_metdata
from json import loads, dumps


# resonanceUrl = 'https://www.youtube.com/watch?v=LZ4ug8Nc0Q8'


# smittyVideo = 'https://youtu.be/u8sRY0tKTuc?si=XsVdOj9-vLfPAoFq'


# output = get_link_metdata(smittyVideo)

# outputJson = loads(output)



def _extract_metadata(info: dict):
    return (
        info['uploader'],
        info['title'],
        info['duration_string'],
        info['thumbnail']
    )






with open('stuff.json', 'r') as f:
    outputJson = loads(f.read())
















# # print(f'Uploader: {outputJson['uploader']}')
# # print(f'Title: {outputJson['title']}')
# # print(f'Duration: {outputJson['duration_string']}')
# # print(f'ThumbnailUrl: {outputJson['thumbnail']}')


# formatsDict = outputJson['formats']


# print(dumps(formatsDict))




print('+'.join(['1']))