#!/usr/bin/python3
"""Test module for the State Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class representing unittest for State"""
    test_state = State()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(State, type(self.test_state))
        self.assertTrue(hasattr(self.test_state, "id"))
        self.assertTrue(hasattr(self.test_state, "created_at"))
        self.assertTrue(hasattr(self.test_state, "updated_at"))
        self.assertTrue(hasattr(self.test_state, "name"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_state.name))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[State] ({}) {}".format(
            self.test_state.id, self.test_state.__dict__)
        self.assertEqual(str(self.test_state), output)


if __name__ == "__main__":
    unittest.main()
