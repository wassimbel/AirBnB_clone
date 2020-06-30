#!/usr/bin/python3
""" module - Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ subclass Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ self """
        super().__init__(self, *args, **kwargs)
