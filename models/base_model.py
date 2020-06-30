#!/usr/bin/python3
""" module - class BaseModel tha defines all common
    attributes/methods for other classes """
from datetime import datetime
import uuid
import models
t = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ class BaseModel: to take care of the initialization, serialization and
        deserialization of future instances """
    def __init__(self, *args, **kwargs):
        """ instantiates id with an uuid when an instance is created """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at"):
                self.created_at = datetime.strptime(kwargs["created_at"], t)
            if hasattr(self, "updated_at"):
                self.updated_at = datetime.strptime(kwargs["updated_at"], t)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
             with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance: """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
