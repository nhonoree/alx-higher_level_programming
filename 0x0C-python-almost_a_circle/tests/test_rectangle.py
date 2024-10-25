import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
<<<<<<< HEAD
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
=======
    def test_initialization(self):
        r = Rectangle(4, 5, 2, 3, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_str_method(self):
        r = Rectangle(4, 5, 4, 5, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 4/5")

    def test_to_dictionary(self):
        r = Rectangle(5, 6, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 6, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)
>>>>>>> d0c69920a5afaafdc65beee62b8aef2ff22b8d19
