#!/usr/bin/python3
""" State Class Unittest """
import unittest
from models.state import State
from models.base_model import BaseModel

class Test_State(unittest.TestCase):
    """ State class testing """

    def setUp(self):
        """setup"""
        self.S = State()

    def test_state(self):
        """ test """
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))

    def test_str(self):
        """ test print """
        str = "[{}] ({}) {}".format("State", self.S.id,
                                    self.S.__dict__)
        self.assertEqual(print(str), print(self.S))

    def test_to_dict(self):
        """to_dict testing"""
        dic = State()
        self.assertIsInstance(dic.to_dict(), dict)

    def test_to_dict(self):
        """Test dict"""
        self.assertIsInstance(self.S.to_dict(), dict)

    def test_id(self):
        """ id testing """
        s = State()
        s1 = State()
        self.assertNotEqual(s.id, s1.id)

    def test_doc_1(self):
        """ test """
        test = "  subclass State "
        test1 = State.__doc__
        self.assertEqual(test, test1)


if __name__ == '__main__':
    unittest.main()

