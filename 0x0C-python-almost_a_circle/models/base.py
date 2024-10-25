#!/usr/bin/python3


""" Base class for all models """


class Base:
    """ A base class for all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
