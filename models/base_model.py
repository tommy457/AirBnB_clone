#!/usr/bin/puthon3
"""Module for BaseModel Class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class representing base module for the project"""
    def __init__(self, *args, **kwargs):
        """Constractor"""
        if kwargs != {} and kwargs is not None:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Method for updating updated_at attribute"""
        self.updated_at = datetime.today()
        models.storage.save()

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
