import unittest
from rectangle import Rectangle
from square import Square

class TestShapes(unittest.TestCase):
    def test_rectangle_creation(self):
        rect = Rectangle(3, 4, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.id, 1)

    def test_square_creation(self):
        square = Square(7, 3)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.id, 3)

    def test_rectangle_area(self):
        rect = Rectangle(3, 4, 1)
        self.assertEqual(rect.area(), 12)

    def test_square_area(self):
        square = Square(7, 3)
        self.assertEqual(square.area(), 49)

if __name__ == '__main__':
    unittest.main()
