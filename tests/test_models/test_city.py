#!/usr/bin/python3
""" City Class Unittest """
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """ City class testing """
    def setUp(self):
        """setup"""
        self.user = City()


    def test_city(self):
        """ test """
        c = City()
        self.assertTrue(hasattr(c, "name"))
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("City", self.user.id,
                                    self.user.__dict__)
        self.assertEqual(print(str), print(self.user))

    def test_to_dict(self):
        """to_dict testing"""
        dic = City()
        self.assertIsInstance(dic.to_dict(), dict)

    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.user.to_dict(), dict)

    def test_id(self):
        """ id testing """
        u = City()
        u1 = City()
        self.assertNotEqual(u.id, u1.id)

    def test_doc_1(self):
        """ test """
        test = " subclass City "
        test1 = City.__doc__
        self.assertEqual(test, test1)

if __name__ == '__main__':
    unittest.main()

