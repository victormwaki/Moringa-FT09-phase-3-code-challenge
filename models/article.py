import sqlite3
from database.connection import get_db_connection

class Article:
    def __init__(self, id=None, title=None, content=None, author_id=None, magazine_id=None):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("Content must be a non-empty string.")
        if not isinstance(author_id, int):
            raise ValueError("Author ID must be an integer.")
        if not isinstance(magazine_id, int):
            raise ValueError("Magazine ID must be an integer.")

        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        if not id:  # Insert the article into the database
            self._id = self._create_article_in_db()

    def _create_article_in_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
            ''',
            (self._title, self._content, self._author_id, self._magazine_id)
        )
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return article_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._update_field_in_db("title", value)
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content must be a non-empty string.")
        self._update_field_in_db("content", value)
        self._content = value

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Author ID must be an integer.")
        self._update_field_in_db("author_id", value)
        self._author_id = value

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Magazine ID must be an integer.")
        self._update_field_in_db("magazine_id", value)
        self._magazine_id = value

    def _update_field_in_db(self, field, value):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"UPDATE articles SET {field} = ? WHERE id = ?"
        cursor.execute(query, (value, self._id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Article(
                id=row[0],
                title=row[1],
                content=row[2],
                author_id=row[3],
                magazine_id=row[4],
            )
        return None

    @staticmethod
    def delete(article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Article {self.title}>"
