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
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))

    def test_kwargs(self, *args, **kwargs):
        """ testing args and kwargs """
        pass

    def test_str(self):
        """ test print """
    str = "[{}] ({}) {}".format("BaseModel", self.base.id, self.base.__dict__)
        self.assertEqual(print(str), print(self.base))

    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.base.to_dict(), dict)

if __name__ == '__main__':
    unittest.main()
