#################################################################
# Python Lib Imports 

from enum import StrEnum


#################################################################
# Links Table

class Media(StrEnum):
    TABLE_NAME = 'Media'
    ID = 'id'
    UUID = 'uuid'
    HOST = 'host'
    UPLOADER = 'uploader'
    TITLE = 'title'
    DURATION = 'duration'


class Links(StrEnum):
    TABLE_NAME = 'Links'
    MEDIA_ID = 'media_id'
    URL = 'url'


class Videos(StrEnum):
    TABLE_NAME = 'Videos'
    MEDIA_ID = 'media_id'
    PATH = 'path'
    SIZE = 'size'
    RESOLUTION = 'resolution'
    FPS = 'fps'
    FORMAT = 'format'
    

class Audio(StrEnum):
    TABLE_NAME = 'Audio'
    MEDIA_ID = 'media_id'
    PATH = 'path'
    SIZE = 'size'
    FORMAT = 'format'

