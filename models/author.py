from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id  
        self._name = name
        self._create_author()

    def _create_author(self):
        pass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @classmethod
    def create(cls, name):
        """Inpuy an author into the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Display authors from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['name']) for row in rows]
    
    def __repr__(self):
        return f'<Author {self.name}>'
    
authors = Author.get_all()
for author in authors:
    print(author)
