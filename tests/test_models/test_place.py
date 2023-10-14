#!/usr/bin/python3
"""Test module for the Place Class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class representing unittest for Place"""
    test_place = Place()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(Place, type(self.test_place))
        self.assertTrue(hasattr(self.test_place, "id"))
        self.assertTrue(hasattr(self.test_place, "created_at"))
        self.assertTrue(hasattr(self.test_place, "updated_at"))
        self.assertTrue(hasattr(self.test_place, "name"))
        self.assertTrue(hasattr(self.test_place, "description"))
        self.assertTrue(hasattr(self.test_place, "number_rooms"))
        self.assertTrue(hasattr(self.test_place, "number_bathrooms"))
        self.assertTrue(hasattr(self.test_place, "max_guest"))
        self.assertTrue(hasattr(self.test_place, "price_by_night"))
        self.assertTrue(hasattr(self.test_place, "latitude"))
        self.assertTrue(hasattr(self.test_place, "longitude"))
        self.assertTrue(hasattr(self.test_place, "state_id"))
        self.assertTrue(hasattr(self.test_place, "city_id"))
        self.assertTrue(hasattr(self.test_place, "user_id"))
        self.assertTrue(hasattr(self.test_place, "amenity_ids"))

    def test_attrs_type(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_place.name))
        self.assertEqual(str, type(self.test_place.description))
        self.assertEqual(int, type(self.test_place.number_rooms))
        self.assertEqual(int, type(self.test_place.number_bathrooms))
        self.assertEqual(int, type(self.test_place.max_guest))
        self.assertEqual(int, type(self.test_place.price_by_night))
        self.assertEqual(float, type(self.test_place.latitude))
        self.assertEqual(float, type(self.test_place.longitude))
        self.assertEqual(str, type(self.test_place.state_id))
        self.assertEqual(str, type(self.test_place.city_id))
        self.assertEqual(str, type(self.test_place.user_id))
        self.assertEqual(str, type(self.test_place.amenity_ids))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[Place] ({}) {}".format(
            self.test_place.id, self.test_place.__dict__)
        self.assertEqual(str(self.test_place), output)


if __name__ == "__main__":
    unittest.main()
