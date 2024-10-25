<<<<<<< HEAD
class Rectangle:
    _id_counter = 1  # Class variable to keep track of IDs

    def __init__(self, width, height, id=None):
        if id is None:
            self.id = Rectangle._id_counter
            Rectangle._id_counter += 1
        else:
            self.id = id
=======
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value
=======
        self.__width = value
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.height):
            print('#' * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.width}/{self.height"

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height}
=======
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
