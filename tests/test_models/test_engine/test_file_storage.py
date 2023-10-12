#!/usr/bin/python3
"""Test module for the FileStorage Class"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Class representing unittest for FileStorage"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test__attributes(self):
        """Test method for class attributes"""
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertEqual(type(storage).__name__, "FileStorage")
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all(self):
        """Unit test for the all method"""
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """Unit test for the new method"""
        test_model = BaseModel()
        storage.new(test_model)
        key = "{}.{}".format(type(test_model).__name__, test_model.id)

        self.assertIn(key, storage.all().keys())
        self.assertIn(test_model, storage.all().values())

    def test_save(self):
        """Unit test for the save method"""
        test_model = BaseModel()
        storage.new(test_model)
        storage.save()
        key = "{}.{}".format(type(test_model).__name__, test_model.id)
        output = ""

        with open("file.json", "r") as f:
            output = f.read()
            self.assertIn(key, output)

    def test_reload(self):
        """Unit test for the reload method"""
        test_model = BaseModel()
        storage.new(test_model)
        storage.save()
        storage.reload()
        key = "{}.{}".format(type(test_model).__name__, test_model.id)
        objs = FileStorage._FileStorage__objects

        self.assertIn(key, objs)


if __name__ == "__main__":
    unittest.main()
