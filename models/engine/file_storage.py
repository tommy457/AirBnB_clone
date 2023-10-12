#!/usr/bin/puthon3
"""Module for FileStorage Class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class representing storage module for the project"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that return __objects dict"""
        return FileStorage.__objects

    def new(self, obj):
        """MEthod that sets new obj in __objects dict"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Method tha serializes __objects dict to the JSON file"""
        objdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Method tha deserializes the JSON file to __objects dict"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
