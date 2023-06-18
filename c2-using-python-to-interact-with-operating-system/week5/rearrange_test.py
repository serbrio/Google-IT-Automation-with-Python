#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest
import os

class TestRearrange(unittest.TestCase):
    def setUp(self):
        self.temp_file_name = "testing_file_open_for_write"
        self.f = open(self.temp_file_name, 'w')
    def test_basic(self):
        testcase = "Lovegod, Luna"
        expected = "Luna Lovegod"
        self.assertEqual(rearrange_name(testcase), expected)
    
    
    def test_empty(self):
        testcase = ""
        expected = testcase 
        self.assertEqual(rearrange_name(testcase), expected)
        

    def test_one_name(self):
        testcase = "Manya"
        expected = "Manya"
        self.assertEqual(rearrange_name(testcase), expected)
    
    
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
        
    
    def test_file_descriptor_instead_name(self):
        with self.assertRaises(TypeError):
            rearrange_name(self.f)
            
    
    def test_file_descriptor_given_to_callable(self):
        self.assertRaises(TypeError, rearrange_name, self.f)
    
    
    def tearDown(self):
        self.f.close()
        os.remove(self.temp_file_name)
        
    
if __name__ == "__main__":
    unittest.main()
