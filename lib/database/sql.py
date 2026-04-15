#################################################################
# Local Imports

from .schemas import Media, Links


#################################################################
# SQL to activate foreign keys

FOREIGN_KEYS = 'PRAGMA foreign_keys = ON;'


#################################################################
# SQL for creating tables

# INIT_TABLES = f'''
# CREATE TABLE IF NOT EXISTS {Pending.TABLE_NAME} (
#     {Pending.UUID} TEXT PRIMARY KEY,
#     {Pending.JSON} TEXT NOT NULL
# ) STRICT;

# CREATE TABLE IF NOT EXISTS {Files.TABLE_NAME} (
#     {Files.ID} INTEGER PRIMARY KEY,
#     {Files.PATH} TEXT NOT NULL,
#     {Files.TYPE} TEXT NOT NULL CHECK ({Files.TYPE} in ('{TypeValues.VIDEO}', '{TypeValues.AUDIO}')),
#     {Files.SIZE} TEXT NOT NULL,
#     {Files.RESOLUTION} TEXT NOT NULL,
#     {Files.FPS} INTEGER NOT NULL,
#     {Files.UPLOADER} TEXT NOT NULL,
#     {Files.TITLE} TEXT NOT NULL,
#     {Files.DURATION} TEXT NOT NULL
# ) STRICT;
# '''

INIT_TABLES = f'''
CREATE TABLE IF NOT EXISTS {Media.TABLE_NAME} (
    {Media.ID} INTEGER PRIMARY KEY,
    {Media.UUID} TEXT NOT NULL,
    {Media.HOST} TEXT NOT NULL,
    {Media.UPLOADER} TEXT NOT NULL,
    {Media.TITLE} TEXT NOT NULL,
    {Media.DURATION} TEXT NOT NULL
) STRICT;

CREATE TABLE IF NOT EXISTS {Links.TABLE_NAME} (
    {Links.MEDIA_ID} INTEGER NOT NULL,



    FOREIGN KEY({Links.MEDIA_ID}) REFERENCES {Media.TABLE_NAME}({Media.ID})

) STRICT;
'''






#################################################################
# SQL for inserting values

# INSERT_PENDING = f'''
# INSERT INTO {Pending.TABLE_NAME}
# ({Pending.UUID},
# {Pending.JSON})
# VALUES (?, ?);
# '''


# INSERT_FILE = f'''
# INSERT INTO {Files.TABLE_NAME}
# ({Files.ID},
# {Files.PATH},
# {Files.TYPE},
# {Files.SIZE},
# {Files.RESOLUTION},
# {Files.FPS},
# {Files.UPLOADER},
# {Files.TITLE},
# {Files.DURATION})
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# '''


#################################################################
# SQL for removing values


# DELETE_PENDING = f'''
# DELETE FROM {Pending.TABLE_NAME}
# WHERE {Pending.UUID} = ?;
# '''