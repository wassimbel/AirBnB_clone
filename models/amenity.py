#!/usr/bin/python3
""" module -  Amenity Class that inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ subclass Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """self """
        super().__init__(self, *args, **kwargs)
