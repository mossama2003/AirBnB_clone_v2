#!/usr/bin/python3
""" Test suite for the console"""

import os
import sys
import models
from unittest.mock import patch
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
import os


class test_console(unittest.TestCase):
    """Class to test the console"""

    def setUp(self):
        """Set up for the tests"""
        self.consol = HBNBCommand()

    def tearDown(self):
        """Clean everything up after running setup"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_create(self):
        """Test the create command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[State] (uuid)\n")

    def test_show(self):
        """Test the show command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd("show State uuid")
            self.assertEqual(f.getvalue(), "[State] (uuid) {'name': 'California'}\n")

    def test_destroy(self):
        """Test the destroy command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd("destroy State uuid")
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_all(self):
        """Test the all command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd("all State")
            self.assertEqual(f.getvalue(), "[State] (uuid) {'name': 'California'}\n")

    def test_update(self):
        """Test the update command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd('update State uuid name "New Mexico"')
            self.consol.onecmd("show State uuid")
            self.assertEqual(f.getvalue(), "[State] (uuid) {'name': 'New Mexico'}\n")

    def test_quit(self):
        """Test the quit command"""
        with self.assertRaises(SystemExit):
            self.consol.onecmd("quit")

    def test_EOF(self):
        """Test the EOF command"""
        with self.assertRaises(SystemExit):
            self.consol.onecmd("EOF")

    def test_help(self):
        """Test the help command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("help")
            self.assertEqual(
                f.getvalue(),
                "Documented commands (type help <topic>):\n========================================\nEOF  all  count  create  destroy  help  quit  show  update\n\n",
            )

    def test_count(self):
        """Test the count command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            self.consol.onecmd("count State")
            self.assertEqual(f.getvalue(), "1\n")
