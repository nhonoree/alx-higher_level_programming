# tests/test_base.py
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def setUp(self):
        """ Reset the ID before each test """
        Base._Base__nb_objects = 0

    def test_base_default_id(self):
        """Test if id is automatically assigned correctly"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_custom_id(self):
        """Test custom id assignment"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_base_id_increment(self):
        """Test that id increments when no id is passed"""
        b4 = Base()
        self.assertEqual(b4.id, 1)
        b5 = Base()
        self.assertEqual(b5.id, 2)

if __name__ == "__main__":
    unittest.main()
