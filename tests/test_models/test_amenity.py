#!/usr/bin/python3
""" Amenity Class Unittest """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os

class Test_Amenity(unittest.TestCase):
    """ Amenity class testing """
    def setUp(self):
        """setup"""
        self.am = Amenity()

    def test_amenity(self):
        """ test """
        a = Amenity()
        self.assertTrue(hasattr(self.am, "name"))
        self.assertTrue(hasattr(self.am, "id"))
        self.assertTrue(hasattr(self.am, "created_at"))
        self.assertTrue(hasattr(self.am, "updated_at"))
        self.assertTrue(issubclass(Amenity, BaseModel))
        a = Amenity()
        a.name = "Holberton"
        a.my_number = 89
        a.id = 1
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "my_number"))
        self.assertEqual(a.name, "Holberton")
        self.assertEqual(a.my_number, 89)
        self.assertNotEqual(a.id, self.am.id)
        self.assertEqual(a.id, 1)
        self.assertTrue(os.path.exists("file.json"))

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("Amenity", self.am.id,
                                    self.am.__dict__)
        self.assertEqual(print(str), print(self.am))

    def test_to_dict(self):
        """to_dict testing"""
        dic = Amenity()
        self.assertIsInstance(dic.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
