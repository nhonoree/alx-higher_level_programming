<<<<<<< HEAD
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, id=None):
        super().__init__(size, size, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"[Square] ({self.id}) {self.size}/{self.size}"

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size}
=======
"""Square class that inherits from Rectangle."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.size}/{self.size}"

    # Additional methods...
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
