#!/usr/bin/python3
"""Unittest for class FileStorage """

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage"""

    def test_init(self):
        """ test """
        f = FileStorage()
        self.assertIsInstance(f, FileStorage)
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        self.assertEqual(b, f.all()["BaseModel" + "." + b.id])

    def test_a(self):
        """ testing  """
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        f.save()
        test = f.all()
        f.reload()
        self.assertEqual(test, f.all())

    def test_file(self):
        """ testing file_path """
        test = FileStorage()
        self.assertIsInstance(test._FileStorage__file_path, str)
        self.assertTrue(os.path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
