# tests/test_square.py

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_initialization(self):
        """Test proper initialization of Square object"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)

    def test_area(self):
        """Test area calculation for Square"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_invalid_size_type(self):
        """Test that an error is raised for invalid size type"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_invalid_size_value(self):
        """Test that an error is raised for invalid size value"""
        with self.assertRaises(ValueError):
            Square(-5)

    # Add more tests for methods like display, update, etc.

if __name__ == '__main__':
    unittest.main()
