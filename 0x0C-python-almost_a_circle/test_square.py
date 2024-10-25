"""Unit tests for the Square class."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_initialization(self):
        """Test initialization of Square."""
        s = Square(4)
        self.assertEqual(s.size, 4)

    def test_str_method(self):
        """Test the __str__ method."""
        s = Square(4, id=10)
        self.assertEqual(str(s), "[Square] (10) 4/4")

    # Additional test methods...
