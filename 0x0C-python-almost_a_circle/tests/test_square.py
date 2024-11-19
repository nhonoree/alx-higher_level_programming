#!/usr/bin/python3
<<<<<<< HEAD
=======
""" Test Square class """

>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
<<<<<<< HEAD
    """ Test the Square class """

    def test_initialization(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=10, size=20, x=30, y=40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)
=======
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
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40


if __name__ == '__main__':
    unittest.main()
