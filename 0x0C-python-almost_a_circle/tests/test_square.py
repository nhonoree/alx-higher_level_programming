import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area, 25)

    def test_str_method(self):
        s = Square(5, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(0)


if __name__ == "__main__":
    unittest.main()
