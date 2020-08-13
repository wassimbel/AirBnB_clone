#!/usr/bin/python3
""" module -  class City that inhertis from BaseModel """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ subclass City """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """  """
        super().__init__(self, *args, **kwargs)
