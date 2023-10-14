#!/usr/bin/python3
"""Module for the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Subclass representing a city inherits from BaseModel"""
    name = ""
    state_id = ""
