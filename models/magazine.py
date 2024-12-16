from database.connection import get_db_connection 

class Magazine:
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category
        
    def _create_magazine(self):
        pass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category
    
    @classmethod
    def create(cls, name, category):
        """Input a new magazine into the database."""
        conn = get_db_connection()  
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Display magazines from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['name'], row['category']) for row in rows]  

    def __repr__(self):
        return f"<Magazine {self.name} ({self.category})>"
    
 

    

    
    
