from models.rectangle import Rectangle

class Square(Rectangle):
<<<<<<< HEAD
    def __init__(self, size, id=None):
        super().__init__(size, size, id)
        self.size = size
=======
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

<<<<<<< HEAD
    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"[Square] ({self.id}) {self.size}/{self.size}"

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size}
=======
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
