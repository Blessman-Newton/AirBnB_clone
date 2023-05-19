#!/usr/bin/python3
"""
test_console.py
"""
import sys
import unittest
import inspect
import io
import pep8
from contextlib import redir_to_stdout
from console import ALXCommand


class TestALXCommand(unittest.TestCase):
    """
    class for testing ALXCommand class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(ALXCommand, inspect.isfunction)

    def test_pep8_conformance_ALXCommand(self):
        """
        Test that console.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_ALXCommand(self):
        """
        Test that test_console.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(ALXCommand.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(ALXCommand.__doc__) >= 1)
