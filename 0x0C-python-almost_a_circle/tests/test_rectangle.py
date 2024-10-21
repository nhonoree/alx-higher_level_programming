# tests/test_rectangle.py
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_initialization(self):
        """Test initialization of Rectangle"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)

    def test_rectangle_area(self):
        """Test the area calculation of Rectangle"""
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    # Add more tests for other attributes and methods

if __name__ == "__main__":
    unittest.main()
