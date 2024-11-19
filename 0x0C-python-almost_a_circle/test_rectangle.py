"""Unit tests for the Rectangle class."""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_initialization(self):
        """Test initialization of Rectangle."""
        r = Rectangle(4, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

    def test_str_method(self):
        """Test the __str__ method."""
        r = Rectangle(4, 5, id=10)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5")

    # Additional test methods...
