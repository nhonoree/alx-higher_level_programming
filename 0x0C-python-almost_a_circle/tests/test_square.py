import unittest
from models.square import Square
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up a new Square instance for testing."""
        self.square1 = Square(5)
        self.square2 = Square(10, 2, 3, 1)

    def test_area(self):
        """Test the area calculation."""
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 100)

    def test_position(self):
        """Test the position of the square."""
        self.assertEqual(self.square2.x, 2)
        self.assertEqual(self.square2.y, 3)

    def test_str_method(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.square1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(self.square2), "[Square] (1) 2/3 - 10")

    def test_update(self):
        """Test the update method."""
        self.square1.update(2, 7, 1, 2)
        self.assertEqual(self.square1.id, 2)
        self.assertEqual(self.square1.size, 7)
        self.assertEqual(self.square1.x, 1)
        self.assertEqual(self.square1.y, 2)

if __name__ == "__main__":
    unittest.main()
