#!/usr/bin/python3
""" module - class FileStorage """
import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from os import path


class FileStorage:
    """class FileStorage  that serializes instances to a
       JSON file and deserializes JSON file to instances"""
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Place": Place,
               "Review": Review, "Amenity": Amenity}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        if self.__file_path:
            json_obj = {}
            for key in FileStorage.__objects:
                json_obj[key] = FileStorage.__objects[key].to_dict()
            with open(FileStorage.__file_path, mode="w", encoding="utf-8")as f:
                json.dump(json_obj, f)

    def reload(self):
        """ deserializes the JSON file """
        f_path = FileStorage.__file_path
        try:
            with open(f_path, mode='r', encoding='utf-8') as f:
                from_json = json.load(f)
        except:
            return
        for key, value in from_json.items():
            cls = value['__class__']
            FileStorage.__objects[key] = FileStorage.classes[cls](**value)
