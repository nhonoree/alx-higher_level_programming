#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is not int or value <= 0:
            raise ValueError("width must be a positive integer")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) is not int or value <= 0:
            raise ValueError("height must be a positive integer")
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("x must be a non-negative integer")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("y must be a non-negative integer")
        self._y = value
