# tests/test_square.py
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_initialization(self):
        """Test initialization of Square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_square_area(self):
        """Test the area calculation of Square"""
        s2 = Square(4)
        self.assertEqual(s2.area(), 16)

    # Add more tests for methods like update() and to_dictionary()

if __name__ == "__main__":
    unittest.main()
