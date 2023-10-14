#!/usr/bin/python3
"""Module for the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Subclass representing a review inherits from BaseModel"""
    text = ""
    place_id = ""
    user_id = ""
