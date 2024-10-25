<<<<<<< HEAD
=======
# base.py
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
class Base:
    """A simple base class for future shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
