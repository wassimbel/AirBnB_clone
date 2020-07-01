#!/usr/bin/python3
""" unittest for User """

import unittest
import os
from models.base_model import BaseModel
from models.user import User
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ class User """

    def setUp(self):
        """setup"""
        self.user = User()

    def test_init(self):
        """  instantiation test """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(isinstance(self.user.created_at, datetime))
        self.assertTrue(isinstance(self.user.updated_at, datetime))
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertTrue(issubclass(User, BaseModel))
        u = User()
        u.name = "Holberton"
        u.my_number = 89
        u.id = 1
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "name"))
        self.assertTrue(hasattr(u, "my_number"))
        self.assertEqual(u.name, "Holberton")
        self.assertEqual(u.my_number, 89)
        self.assertNotEqual(u.id, self.user.id)
        self.assertEqual(u.id, 1)
        self.assertTrue(os.path.exists("file.json"))
        test = User(**self.user.to_dict())
        self.assertEqual(test.id, self.user.id)

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("User", self.user.id,
                                    self.user.__dict__)
        self.assertEqual(print(str), print(self.user))

    def test_to_dict(self):
        """to_dict testing"""
        dic = User()
        self.assertIsInstance(dic.to_dict(), dict)

    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.user.to_dict(), dict)

    def test_id(self):
        """ id testing """
        u = User()
        u1 = User()
        self.assertNotEqual(u.id, u1.id)

if __name__ == '__main__':
    unittest.main()
