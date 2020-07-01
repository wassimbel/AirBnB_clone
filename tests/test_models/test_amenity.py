#!/usr/bin/python3
""" Amenity Class Unittest """
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Amenity class testing """

    def test_amenity(self):
        """ test """
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))


if __name__ == '__main__':
    unittest.main()
