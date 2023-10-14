#!/usr/bin/python3
"""Test module for the Amenity Class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class representing unittest for Amenity"""
    test_amenity = Amenity()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(Amenity, type(self.test_amenity))
        self.assertTrue(hasattr(self.test_amenity, "id"))
        self.assertTrue(hasattr(self.test_amenity, "created_at"))
        self.assertTrue(hasattr(self.test_amenity, "updated_at"))
        self.assertTrue(hasattr(self.test_amenity, "name"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_amenity.name))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[Amenity] ({}) {}".format(
            self.test_amenity.id, self.test_amenity.__dict__)
        self.assertEqual(str(self.test_amenity), output)


if __name__ == "__main__":
    unittest.main()
