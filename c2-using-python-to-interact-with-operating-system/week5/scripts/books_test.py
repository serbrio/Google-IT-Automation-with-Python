#!/usr/bin/env python3

import unittest
from books import find_book

class TestFindBook(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_book('Момо'), [('available', 'not read', 'Энде (Момо)')])

    def test_not_found(self):
        self.assertEqual(find_book('Nosuchbookexists'), [])

    def test_empty(self):
        pass


if __name__ == "__main__":
    unittest.main()
