#!/usr/bin/python3
""" Review Class Unittest """
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Amenity class testing """

    def test_review(self):
        """ test """
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))


if __name__ == '__main__':
    unittest.main()

