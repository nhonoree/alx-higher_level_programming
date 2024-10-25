"""Unit tests for the Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_assignment(self):
        """Test the ID assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_assignment_with_value(self):
        """Test the ID assignment with a specific value."""
        b2 = Base(42)
        self.assertEqual(b2.id, 42)

    # Additional test methods...
