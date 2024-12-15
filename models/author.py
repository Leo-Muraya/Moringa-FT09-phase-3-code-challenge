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
