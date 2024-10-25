import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
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
