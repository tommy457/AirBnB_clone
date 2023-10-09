#!/usr/bin/puthon3
"""Module for BaseModel Class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class representing base module for the project"""
    def __init__(self):
        """Constractor"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Method for updating updated_at attribute"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Method that returns a dictionary of __dict__ of the instance"""
        resdict = self.__dict__.copy()
        resdict["__class__"] = self.__class__.__name__
        resdict["created_at"] = self.created_at.isoformat()
        resdict["updated_at"] = self.updated_at.isoformat()

        return resdict

    def __str__(self):
        """Magic method returns the string representation of the object"""
        classname = self.__class__.__name__

        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
