"""Test module for the BaseModule Class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModule(unittest.TestCase):
    """Class representing test for BaseModel"""
    test_model_1 = BaseModel()
    sleep(0.1)
    test_model_2 = BaseModel()

    def test_create_and_init(self):
        """Test method for creating a new instance"""
        self.assertEqual(BaseModel, type(self.test_model_1))
        self.assertTrue(hasattr(self.test_model_1, "id"))
        self.assertTrue(hasattr(self.test_model_1, "created_at"))
        self.assertTrue(hasattr(self.test_model_1, "updated_at"))

    def test_id(self):
        """Test Method that checks id type"""
        self.assertEqual(str, type(self.test_model_1.id))

    def test_uniq_id(self):
        """Test Method that checks id of two instances is uniq"""
        self.assertNotEqual(self.test_model_1.id, self.test_model_2.id)

    def test_created_at(self):
        """Test Method that checks created_at is datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_creations_time(self):
        """Test Method that checks created_at of two instances is diffrent"""
        self.assertNotEqual(
            self.test_model_1.created_at, self.test_model_2.created_at)

    def test_updated_at(self):
        """Test Method that checks updated_at is datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_updating_time(self):
        """Test Method that checks updated_at of two instances is diffrent"""
        self.test_model_1.save()
        self.assertNotEqual(
            self.test_model_1.created_at, self.test_model_1.updated_at)

    def test_to_dict(self):
        """Test Method that checks to_dict return type"""
        self.assertTrue(dict, type(self.test_model_1.to_dict()))

    def test_to_dict_keys(self):
        """Test Method that checks to_dict all keys exits"""
        self.assertIn("id", self.test_model_1.to_dict())
        self.assertIn("created_at", self.test_model_1.to_dict())
        self.assertIn("updated_at", self.test_model_1.to_dict())
        self.assertIn("__class__", self.test_model_1.to_dict())

    def test_to_dict_dates(self):
        """Test Method that checks to_dict dates are isoformated"""
        test_dict = self.test_model_1.to_dict()
        self.assertEqual(str, type(test_dict["created_at"]))
        self.assertEqual(str, type(test_dict["updated_at"]))

    def test_str_output(self):
        """Test Method that checks str dunder method return format"""
        output = "[BaseModel] ({}) {}".format(
            self.test_model_1.id, self.test_model_1.__dict__)
        self.assertEqual(str(self.test_model_1), output)


if __name__ == "__main__":
    unittest.main()
