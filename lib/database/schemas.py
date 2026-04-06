#################################################################
# Python Lib Imports 

from enum import StrEnum


#################################################################
# Pending Table schemas

class Pending(StrEnum):
    TABLE_NAME = 'Pending'
    UUID = 'uuid'
    JSON = 'json'


#################################################################
# Files Table schemas

class Files(StrEnum):
    TABLE_NAME = 'Files'
    ID = 'id'
    PATH = 'path'
    TYPE = 'type'
    SIZE = 'size'
    RESOLUTION = 'resolution'
    FPS = 'fps'
    UPLOADER = 'uploader'
    TITLE = 'title'
    DURATION = 'duration'


class TypeValues(StrEnum):
    VIDEO = 'video'
    AUDIO = 'audio'