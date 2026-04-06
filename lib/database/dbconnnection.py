#################################################################
# Python Lib Imports 

from sqlite3 import connect, Connection, Row
from os.path import join


#################################################################
# Local Imports

from .sql import INIT_TABLES, FOREIGN_KEYS, INSERT_PENDING, DELETE_PENDING
from ..config import DB_DIR


#################################################################
# DBConnection Class


class DBConnection:
    '''Manages connection to database defined by DB_PATH config'''

    def __init__(self):
        # set connection to None so that context manager handles creating connection
        self.conn: Connection | None = None


    def __enter__(self):
        # connect to database
        self.conn = connect(join(DB_DIR, 'database.sqlite'))

        # activate foreign keys constraint
        self.conn.execute(FOREIGN_KEYS)

        # initialize tables if they do not exist
        self.conn.executescript(INIT_TABLES)

        # commit changes
        self.conn.commit()

        # return DBConnection object
        return self


    def __exit__(self, exc_type, exc, tb):
        # check if exception type is none
        if exc_type is None:
            # if no exceptions, commit 
            self.conn.commit()

        else:
            # if exception occurred, rollback changes
            self.conn.rollback()

        # close connection and set to None
        self.conn.close()
        self.conn = None


    def insert_pending(self, uuidStr: str, jsonStr: str):
        
        cursor = self.conn.cursor()

        cursor.execute(INSERT_PENDING, (uuidStr, jsonStr))

        cursor.close()


    def remove_pending(self, uuidStr: str):

        cursor = self.conn.cursor()

        cursor.execute(DELETE_PENDING, (uuidStr,))

        cursor.close()