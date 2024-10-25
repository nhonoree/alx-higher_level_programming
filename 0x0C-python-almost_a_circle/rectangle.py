class Rectangle:
    _id_counter = 1  # Class variable to keep track of IDs

    def __init__(self, width, height, id=None):
        if id is None:
            self.id = Rectangle._id_counter
            Rectangle._id_counter += 1
        else:
            self.id = id
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
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
        return f"[Rectangle] ({self.id}) {self.width}/{self.height}"  # Fixed f-string

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height}
