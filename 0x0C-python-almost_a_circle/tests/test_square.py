#!/usr/bin/python3
""" Test Square class """

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """ Tests for the Square class """

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_update_args(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 10)
        self.assertEqual(s.size, 10)
        s.update(89, 10, 1)
        self.assertEqual(s.x, 1)
        s.update(89, 10, 1, 2)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)
        s.update(size=10)
        self.assertEqual(s.size, 10)
        s.update(x=3)
        self.assertEqual(s.x, 3)
        s.update(y=4)
        self.assertEqual(s.y, 4)


if __name__ == '__main__':
    unittest.main()
