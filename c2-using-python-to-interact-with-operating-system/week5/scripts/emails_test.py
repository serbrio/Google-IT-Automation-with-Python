#!/usr/bin/env python3

import unittest
from emails import find_email


class TestFindEmails(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Benedict", "Pacheco"]
        expected = "bpacheco@abc.edu"
        self.assertEqual(find_email(testcase), expected)


if __name__ == "__main__":
    unittest.main()


    
