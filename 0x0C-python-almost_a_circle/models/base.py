import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
