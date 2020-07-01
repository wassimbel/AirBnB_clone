#!/usr/bin/python3
"""Unittest for class FileStorage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


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
