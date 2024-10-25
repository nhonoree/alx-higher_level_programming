<<<<<<< HEAD
=======
#!/usr/bin/python3

""" Rectangle class that inherits from Base """

from models.base import Base


>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
class Rectangle(Base):
    """A class that represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
<<<<<<< HEAD
        """Initialize a Rectangle instance."""
=======
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle (default is 0).
            y (int): The y position of the rectangle (default is 0).
            id (int): The id of the rectangle (default is None).
        """
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
        super().__init__(id)
        self.width = width  # Calls the width setter
        self.height = height  # Calls the height setter
        self.x = x  # Calls the x setter
        self.y = y  # Calls the y setter

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """Set the width of the rectangle, ensuring it's > 0."""
        if not isinstance(value, int) or value <= 0:
=======
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        """Set the height of the rectangle, ensuring it's > 0."""
        if not isinstance(value, int) or value <= 0:
=======
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
<<<<<<< HEAD
        """Get the x coordinate of the rectangle."""
=======
        """Get the x position of the rectangle."""
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
        return self.__x

    @x.setter
    def x(self, value):
<<<<<<< HEAD
        """Set the x coordinate of the rectangle, ensuring it's >= 0."""
        if not isinstance(value, int) or value < 0:
=======
        """Set the x position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
<<<<<<< HEAD
        """Get the y coordinate of the rectangle."""
=======
        """Get the y position of the rectangle."""
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
        return self.__y

    @y.setter
    def y(self, value):
<<<<<<< HEAD
        """Set the y coordinate of the rectangle, ensuring it's >= 0."""
        if not isinstance(value, int) or value < 0:
=======
        """Set the y position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
<<<<<<< HEAD
        """Print the rectangle using '#' characters."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
=======
        """Print the rectangle using '#' character."""
        print("\n" * self.y, end="")  # Create y-offset
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)  # Create x-offset and print

    def __str__(self):
        """Return a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update rectangle attributes."""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """Create a Rectangle instance using a dictionary."""
        return cls(**dictionary)
