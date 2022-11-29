#!/usr/bin/python3
<<<<<<< HEAD
""" Class Review """
=======
<<<<<<< HEAD
"""Contains the Review model"""
=======
"""Defines the Review class."""
>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """ Review class that inherits BaseModel """
=======
<<<<<<< HEAD
    """Implements the Review model"""
=======
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
>>>>>>> d6933edf87fbc1ac580927098c80fed2b66d0899
    place_id = ""
    user_id = ""
    text = ""
