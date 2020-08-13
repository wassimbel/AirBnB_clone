#!/usr/bin/python3
""" state class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """  subclass State """
    name = ""

    def __init__(self, *args, **kwargs):
        """ self """
        super().__init__(self, *args, **kwargs)
