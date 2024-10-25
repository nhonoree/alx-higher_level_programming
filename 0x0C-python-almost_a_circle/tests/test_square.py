import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_initialization(self):
        s = Square(4, 2, 3, 1)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_str_method(self):
        s = Square(4, 4, 4, 10)
        self.assertEqual(str(s), "[Square] (10) 4/4 - 4")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)
