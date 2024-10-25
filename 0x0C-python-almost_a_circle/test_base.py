# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset the __nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_auto_id_increment(self):
        """Test automatic ID assignment"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        """Test custom ID assignment"""
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_empty(self):
        """Test to_json_string method with empty input"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None input"""
        self.assertEqual(Base.to_json_string(None), "[]")

    # Add more tests as needed for other methods like save_to_file, from_json_string, etc.

if __name__ == '__main__':
    unittest.main()
