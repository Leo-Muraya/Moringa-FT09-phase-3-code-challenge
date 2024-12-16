from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._create_article() 

    
    def _create_article(self):
        pass

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id
    
    @title.setter
    def title(self, value):
        """Validate title length (between 5 and 50 characters)."""
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value

    @staticmethod
    def create(title, content, author_id, magazine_id):
        """Create and insert a new article into the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
        ''', (title, content, author_id, magazine_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Display articles from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

        conn.close()

        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]

    def __repr__(self):
        return f'<Article {self.title}>'
    
if __name__ == "__main__":

    articles = Article.get_all()
    for article in articles:
        print(article)
