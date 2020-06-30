#!/usr/bin/python3
""" module - class User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ subclass User """
    email = ""
    password = ""
    fist_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Init user"""
        super().__init__(*args, **kwargs)
