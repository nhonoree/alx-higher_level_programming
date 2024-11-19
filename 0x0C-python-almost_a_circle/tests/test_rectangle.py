#!/usr/bin/python3
<<<<<<< HEAD
=======
""" Test Rectangle class """

>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
<<<<<<< HEAD
    """ Test the Rectangle class """

    def test_initialization(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with self.assertLogs() as log:
            r.display()
            self.assertEqual(log.output, expected_output)

    def test_str(self):
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")

    def test_update_args(self):
        r = Rectangle(3, 4)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_kwargs(self):
        r = Rectangle(3, 4)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

=======
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
>>>>>>> 87f4279dcf8894611017af22dcf0cf8c02b31f40

if __name__ == '__main__':
    unittest.main()
