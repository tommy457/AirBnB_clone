#!/usr/bin/python3
"""Module for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Subclass representing a user inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
