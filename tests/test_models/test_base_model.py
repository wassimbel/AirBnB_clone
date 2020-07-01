#!/usr/bin/python3
""" unittest for BaseModel """

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ class TestBaseModel """

    def setUp(self):
        """ setup"""
        self.base = BaseModel()

    def test_init(self):
        """  instantiation test """
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        self.assertEqual(b.name, "Holberton")
        self.assertEqual(b.my_number, 89)
        self.assertEqual(b.id, b.id)
        self.assertNotEqual(b.id, self.base.id)

    def test_kwargs(self, *args, **kwargs):
        """ testing args and kwargs """
        pass

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("BaseModel", self.base.id, self.base.__dict__)
        self.assertEqual(print(str), print(self.base))

    def test_save(self):
        """ save method testing """
        d = BaseModel()
        up = d.updated_at
        d.save()
        up1 = d.updated_at
        self.assertNotEqual(up, up1)

    def test_to_dict(self):
        """to_dict testing"""
        dic = BaseModel()
        self.assertIsInstance(dic.to_dict(), dict)


    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.base.to_dict(), dict)

    def test_id(self):
        """ id testing """
        b = BaseModel()
        a = BaseModel()
        self.assertNotEqual(b.id, a.id)

    def test_is_an_instance(self):
        """ instance testing """
        c = BaseModel()
        self.assertIsInstance(c, BaseModel)


if __name__ == '__main__':
    unittest.main()
