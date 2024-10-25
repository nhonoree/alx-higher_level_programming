# tests/test_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_initialization(self):
        """Test proper initialization of Rectangle object"""
        rect = Rectangle(3, 5)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area(self):
        """Test area calculation"""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)

    def test_invalid_width_type(self):
        """Test that an error is raised for invalid width type"""
        with self.assertRaises(TypeError):
            Rectangle("3", 5)

    def test_invalid_height_value(self):
        """Test that an error is raised for invalid height value"""
        with self.assertRaises(ValueError):
            Rectangle(3, -5)

    # Add more tests for methods like display, update, etc.

if __name__ == '__main__':
    unittest.main()
