#!/usr/bin/python3
"""
    Testing the file_storage module.
"""

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """
    Testing the file_storage module.
    """

    def setUp(self):
        """
        Initializing instance.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Removing the JSON file.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """
        Testing the all method.
        """
        self.assertEqual(self.storage.all(), {})
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Testing the new method.
        """
        self.storage.new(State())
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        """
        Testing the save method.
        """
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(os.access("file.json", os.R_OK))
        self.assertTrue(os.access("file.json", os.W_OK))
        self.assertTrue(os.path.getsize("file.json") > 0)

    def test_reload(self):
        """
        Testing the reload method.
        """
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_from_nonexistent_file(self):
        """
        Testing the reload method from a nonexistent file.
        """
        self.storage.save()
        os.remove("file.json")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_from_corrupted_file(self):
        """
        Testing the reload method from a corrupted file.
        """
        self.storage.save()
        with open("file.json", "w") as f:
            f.write("Hello")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_from_empty_file(self):
        """
        Testing the reload method from an empty file.
        """
        self.storage.save()
        with open("file.json", "w") as f:
            f.write("")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_from_non_json_file(self):
        """
        Testing the reload method from a non-JSON file.
        """
        self.storage.save()
        with open("file.json", "w") as f:
            f.write("Hello")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_from_valid_file(self):
        """
        Testing the reload method from a valid file.
        """
        self.storage.save()
        with open("file.json", "r") as f:
            json_dict = json.load(f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), len(json_dict))

    def test_reload_from_valid_file_with_one_instance(self):
        """
        Testing the reload method from a valid file with one instance.
        """
        self.storage.save()
        with open("file.json", "r") as f:
            json_dict = json.load(f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), len(json_dict))

    def test_reload_from_valid_file_with_multiple_instances(self):
        """
        Testing the reload method from a valid file with multiple instances.
        """
        self.storage.save()
        with open("file.json", "r") as f:
            json_dict = json.load(f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), len(json_dict))


if __name__ == "__main__":
    unittest.main()
