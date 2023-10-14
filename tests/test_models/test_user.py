#!/usr/bin/python3
"""Test module for the User Class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class representing unittest for User"""
    test_user = User()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(User, type(self.test_user))
        self.assertTrue(hasattr(self.test_user, "id"))
        self.assertTrue(hasattr(self.test_user, "created_at"))
        self.assertTrue(hasattr(self.test_user, "updated_at"))
        self.assertTrue(hasattr(self.test_user, "email"))
        self.assertTrue(hasattr(self.test_user, "password"))
        self.assertTrue(hasattr(self.test_user, "first_name"))
        self.assertTrue(hasattr(self.test_user, "last_name"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_user.email))
        self.assertEqual(str, type(self.test_user.password))
        self.assertEqual(str, type(self.test_user.first_name))
        self.assertEqual(str, type(self.test_user.last_name))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[User] ({}) {}".format(
            self.test_user.id, self.test_user.__dict__)
        self.assertEqual(str(self.test_user), output)


if __name__ == "__main__":
    unittest.main()
