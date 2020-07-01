#!/usr/bin/python3
""" City Class Unittest """
import unittest
from models.city import city


class Test_City(unittest.TestCase):
    """ City class testing """

    def test_city(self):
        """ test """
        c = City()
        self.assertTrue(hasattr(c, "name"))
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))


if __name__ == '__main__':
    unittest.main()

