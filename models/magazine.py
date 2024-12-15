import sqlite3
from database.connection import get_db_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self._id = id
        self._name = name
        self._category = category

        if not id:  # Insert a new magazine into the database
            self._id = self._create_magazine_in_db(name, category)

    def _create_magazine_in_db(self, name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        magazine_id = cursor.lastrowid
        conn.close()
        return magazine_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category


    def __repr__(self):
        return f'<Magazine {self.name}>'
