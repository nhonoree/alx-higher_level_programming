#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """A class that represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle (default is 0).
            y (int): The y position of the rectangle (default is 0).
            id (int): The id of the rectangle (default is None).
        """
        super().__init__(id)  # Call to the superclass constructor
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
