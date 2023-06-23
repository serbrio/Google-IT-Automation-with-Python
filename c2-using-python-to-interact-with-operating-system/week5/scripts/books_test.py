#!/usr/bin/env python3

import unittest
from books import find_book
from books import get_keyword

class TestFindBook(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_book('Момо'), [('[available]', '[not read]', 'Энде (Момо)')])

    def test_not_found(self):
        self.assertEqual(find_book('Nosuchbookexists'), [])

    def test_invalid_type(self):
        self.assertRaises(TypeError, find_book, [])

    def test_none(self):
        self.assertEqual(find_book(None), None)


class TestGetKeyword(unittest.TestCase):
    def test_space(self):
        self.assertEqual(get_keyword([None, " "]), None)

    def test_empty_string(self):
        self.assertEqual(get_keyword([None, ""]), None)

    def test_no_arguments(self):
        self.assertEqaul(get_keyword(["script.py"]), None)


if __name__ == "__main__":
    unittest.main()
