import sqlite3
from .connection import get_db_connection

def create_tables():
    connection = sqlite3.connect('magazine.db')
    cursor = connection.cursor()

    # Authors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    ''')

    # Magazines table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    ''')

    # Articles table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_tables()
