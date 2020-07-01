#!/usr/bin/python3
""" State Class Unittest """
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """ State class testing """

    def test_state(self):
        """ test """
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))


if __name__ == '__main__':
    unittest.main()

