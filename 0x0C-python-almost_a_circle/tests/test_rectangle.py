import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area, 50)

    def test_perimeter(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.perimeter, 30)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_str_method(self):
        r = Rectangle(10, 5, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 10/5")


if __name__ == "__main__":
    unittest.main()
