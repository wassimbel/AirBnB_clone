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
        self.assertIsInstance(test._FileStorage__file_path, str )

    def test_doc_all(self):
        """ test """
        test = " returns the dictionary __objects "
        test1 = FileStorage.all.__doc__
        self.assertEqual(test, test1)

    def test_doc_new(self):
        """ testing """
        test = " sets in __objects the obj with key <obj class name>.id "
        test1 = FileStorage.new.__doc__
        self.assertEqual(test, test1)

    def test_reload(self):
        """ testing """
        test = " deserializes the JSON file "
        test1 = FileStorage.reload.__doc__
        self.assertEqual(test, test1)

    def test_save(self):
        """ testing """
        test = " serializes __objects to the JSON file (path: __file_path) "
        test1 = FileStorage.save.__doc__
        self.assertEqual(test, test1)

if __name__ == '__main__':
    unittest.main()
