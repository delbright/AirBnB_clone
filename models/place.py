#!/usr/bin/python3
<<<<<<< HEAD
""" Class Place """

=======
<<<<<<< HEAD
"""Contains the Place model"""
=======
"""Defines the Place class."""
>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ Place class that inherits BaseModel """
=======
<<<<<<< HEAD
    """
    Implements the Place model

    Args:
=======
    """Represent a place.

    Attributes:
>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
<<<<<<< HEAD
=======

>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
