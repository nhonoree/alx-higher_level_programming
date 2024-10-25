# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    # Additional methods like display, __str__, etc.

