#!/usr/bin/python3
""" Review Class Unittest """
import unittest
from models.review import Review
from models.base_model import BaseModel
import os

class Test_Review(unittest.TestCase):
    """ Amenity class testing """
    def setUp(self):
        """setup"""
        self.R = Review()

    def test_review(self):
        """ test """
        self.assertTrue(hasattr(self.R, "place_id"))
        self.assertTrue(hasattr(self.R, "user_id"))
        self.assertTrue(hasattr(self.R, "text"))
        self.assertTrue(hasattr(self.R, "id"))
        self.assertTrue(hasattr(self.R, "created_at"))
        self.assertTrue(hasattr(self.R, "updated_at"))
        self.assertTrue(issubclass(Review, BaseModel))
        r = Review()
        r.name = "Holberton"
        r.my_number = 89
        r.id = 1
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertTrue(hasattr(r, "name"))
        self.assertTrue(hasattr(r, "my_number"))
        self.assertEqual(r.name, "Holberton")
        self.assertEqual(r.my_number, 89)
        self.assertNotEqual(r.id, self.R.id)
        self.assertEqual(r.id, 1)
        self.assertTrue(os.path.exists("file.json"))

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("Review", self.R.id,
                                    self.R.__dict__)
        self.assertEqual(print(str), print(self.R))

    def test_to_dict(self):
        """to_dict testing"""
        dic = Review()
        self.assertIsInstance(dic.to_dict(), dict)

    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.R.to_dict(), dict)

    def test_id(self):
        """ id testing """
        r = Review()
        r1 = Review()
        self.assertNotEqual(r.id, r1.id)

    def test_doc_1(self):
        """ test """
        test = " subclass Review "
        test1 = Review.__doc__
        self.assertEqual(test, test1)


if __name__ == '__main__':
    unittest.main()

