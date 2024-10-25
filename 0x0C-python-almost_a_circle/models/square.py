#!/usr/bin/python3
""" Square class that inherits from Rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the Square instance with *args or **kwargs """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Return a string representation of the Square instance """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
