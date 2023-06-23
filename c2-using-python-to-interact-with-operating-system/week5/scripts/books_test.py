#!/usr/bin/env python3

import unittest
from books import find_book

class TestFindBook(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_book('Момо'), [('available', 'not read', 'Энде (Момо)')])

    def test_not_found(self):
        self.assertEqual(find_book('Nosuchbookexists'), [])

    def test_space(self):
        self.assertEqual(find_book(' '), [])

    def test_empty_string(self):
        self.assertEqual(find_book(''), [])

    def test_invalid_type(self):
        self.assertRaises(TypeError, find_book, [])

    def test_new(self):
        pass

if __name__ == "__main__":
    unittest.main()
