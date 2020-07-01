#!/usr/bin/python3
"""Unittest for class FileStorage """

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage"""
    def test_init(self):
        """ testin init """
        test = FileStorage()
        self.assertIsInstance(test, FileStorage)
        self.assertEqual(type(test), FileStorage)
        self.assertFalse(hasattr(test, "id"))

    def test_save(self):
        """ testing save """
        test = FileStorage()
        test1 = BaseModel()
        test.new(test1)
        test.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIsInstance(test._FileStorage__objects, dict)

    def test_reload(self):
        """ testing reload """
        test = FileStorage()
        test1 = BaseModel()
        test.new(test1)
        test.save()
        test2 = test.all()
        test.reload()
        self.assertEqual(test2, test.all())

    def test_new(self):
        """ testing new """
        test = FileStorage()
        test1 = BaseModel()
        test.new(test1)
        self.assertEqual(test1, test.all()["BaseModel" + "." + test1.id])

    def test_file_path(self):
        """ testing file_path """
        test = FileStorage()
        self.assertIsInstance(test._FileStorage__file_path, str)

if __name__ == '__main__':
    unittest.main()
