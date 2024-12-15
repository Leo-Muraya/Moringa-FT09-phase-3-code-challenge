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
    
    
