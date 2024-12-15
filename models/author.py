import sqlite3
from database.connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

        self._id = id
        self._name = name

        if not id:  # Insert a new author into the database
            self._id = self._create_author_in_db(name)

    def _create_author_in_db(self, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        author_id = cursor.lastrowid
        conn.close()
        return author_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name of an author after initialization.")

def __repr__(self):
        return f'<Author{self.title}>'