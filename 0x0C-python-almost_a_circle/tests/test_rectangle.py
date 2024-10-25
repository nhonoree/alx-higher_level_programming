#!/usr/bin/python3
""" Test Rectangle class """

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Tests for the Rectangle class """

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "1")
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(2, -1)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "1")
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, "1")
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

if __name__ == '__main__':
    unittest.main()
