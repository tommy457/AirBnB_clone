#!/usr/bin/python3
"""Test module for the City Class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class representing unittest for City"""
    test_city = City()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(City, type(self.test_city))
        self.assertTrue(hasattr(self.test_city, "id"))
        self.assertTrue(hasattr(self.test_city, "created_at"))
        self.assertTrue(hasattr(self.test_city, "updated_at"))
        self.assertTrue(hasattr(self.test_city, "name"))
        self.assertTrue(hasattr(self.test_city, "state_id"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_city.name))
        self.assertEqual(str, type(self.test_city.state_id))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[City] ({}) {}".format(
            self.test_city.id, self.test_city.__dict__)
        self.assertEqual(str(self.test_city), output)


if __name__ == "__main__":
    unittest.main()
