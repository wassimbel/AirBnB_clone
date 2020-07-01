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
        """setup"""
        self.base = BaseModel()

    def test_init(self):
        """  instantiation test """
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertTrue(isinstance(self.base.created_at, datetime))
        self.assertTrue(isinstance(self.base.updated_at, datetime))
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        b.id = 1
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "name"))
        self.assertTrue(hasattr(b, "my_number"))
        self.assertEqual(b.name, "Holberton")
        self.assertEqual(b.my_number, 89)
        self.assertNotEqual(b.id, self.base.id)
        self.assertEqual(b.id, 1)
        self.assertTrue(os.path.exists("file.json"))
        test = BaseModel(**self.base.to_dict())
        self.assertEqual(test.id, self.base.id)
    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("BaseModel", self.base.id,
                                    self.base.__dict__)
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
