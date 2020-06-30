#!/usr/bin/python3
""" module - class HBNBCommaand(cmd.Cmd) """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import argparse


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter
        using cmd module """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def do_quit(self, arg):
        """ command to quit the program """
        return True

    def do_EOF(self, arg):
        """ command ctr-d to quit the program """
        print("KeyboardInterrupt")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id """
        split_ = arg.split()
        if len(split_) < 2:
            if len(split_) == 0:
                print("** class name missing **")
            elif split_[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for key, value in HBNBCommand.classes.items():
                    if split_[0] == key:
                        new = value()
                        new.save()
                        print(new.id)
        else:
            print("number of arg exceeded the max")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id """
        split_ = arg.split()
        if len(split_) < 3:
            if len(split_) == 0:
                print("** class name missing **")
            elif split_[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(split_) == 1:
                print("** instance id missing **")
            elif len(split_) == 2:
                class_id = split_[0] + '.' + split_[1]
                if class_id not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[class_id])
        else:
            print("** too many args **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        split_ = arg.split()
        if len(split_) < 3:
            if len(split_) == 0:
                print("** class name missing **")
            elif split_[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(split_) == 1:
                print("** instance id missing **")
            elif len(split_) == 2:
                class_id = split_[0] + '.' + split_[1]
                if class_id not in storage.all():
                    print("** no instnce found **")
                else:
                    del(storage.all()[class_id])
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
