#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """ A class representing a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height
