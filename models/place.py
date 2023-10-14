#!/usr/bin/python3
"""Module for the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Subclass representing a place inherits from BaseModel"""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    state_id = ""
    city_id = ""
    user_id = ""
    amenity_ids = ""
