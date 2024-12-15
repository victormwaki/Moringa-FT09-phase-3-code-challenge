from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_title = input("Enter magazine title: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create an author
    author = Author(name=author_name)
    print(f"Author Created: ID = {author.id}, Name = {author.name}")

    # Create a magazine
    magazine = Magazine(title=magazine_title, category=magazine_category)
    print(f"Magazine Created: ID = {magazine.id}, name = {magazine.name}, Category = {magazine.category}")

    # Create an article
    article = Article(
        title=article_title,
        content=article_content,
        author_id=author.id,
        magazine_id=magazine.id
    )
    print(f"Article Created: ID = {article.id}, Title = {article.title}, Content = {article.content}")

    # Query all records using model methods (if implemented)
    print("\nAuthors in Database:")
    display_authors()

    print("\nMagazines in Database:")
    display_magazines()

    print("\nArticles in Database:")
    display_articles()


def display_authors():
    """Fetch all authors and display them."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors")
    for row in cursor.fetchall():
        print(Author(id=row[0], name=row[1]))
    conn.close()


def display_magazines():
    """Fetch all magazines and display them."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines")
    for row in cursor.fetchall():
        print(Magazine(id=row[0], title=row[1], category=row[2]))
    conn.close()


def display_articles():
    """Fetch all articles and display them."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles")
    for row in cursor.fetchall():
        print(Article(id=row[0], title=row[1], content=row[2], author_id=row[3], magazine_id=row[4]))
    conn.close()


if __name__ == "__main__":
    main()
