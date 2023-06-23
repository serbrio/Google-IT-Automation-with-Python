#!/usr/bin/env python3

import unittest
from books import find_book
from books import get_keyword
from books import represent_found

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
        self.assertEqual(get_keyword(["script.py"]), None)


class TestRepresentFound(unittest.TestCase):
    def test_none(self):
        self.assertEqual(represent_found(None), "missing keyword")

    def test_empty_found_list(self):
        self.assertEqual(represent_found([]), "not found")


if __name__ == "__main__":
    unittest.main()
