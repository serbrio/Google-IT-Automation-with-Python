#!/usr/bin/env python3

import unittest
from err_stat2csv import rank_errors, sort_users_stat


class TestRankErrors(unittest.TestCase):
    def test_basic(self):
        testcase = ["May 27 11:55:40 ubuntu.local ticky: ERROR: Something failed absolutely (bad_user)",
                    "Feb 10 09:33:13 ubuntu.remote ticky: ERROR: Little thing broken (little_user)",
                    "Jan 24 15:14:24 archlinux ticky: ERROR: Something failed absolutely (arch_user)"]
        expected =[("Something failed absolutely", 2), ("Little thing broken", 1)]
        self.assertEqual(rank_errors(testcase), expected)
    
    def test_error_and_info(self):
        testcase = ["May 13 12:44:32 ubuntu ticky: INFO: Everything fine  [#12345] (info_user)",
                    "Sep 9 06:01:02 windows ticky: ERROR: Browser failed again (admin)",
                    "Jul 18 23:04:43 debian ticky: ERROR: Browser failed again (debian_root)"]
        expected = [("Browser failed again", 2)]
        self.assertEqual(rank_errors(testcase), expected)
        
    def test_no_errors(self):
        testcase = ["May 13 12:44:32 macos ticky: INFO: Everything fine  [#55555] (macoser)"
                    "Jun 23 22:34:36 arch ticky: INFO: Everything fine  [#33333] (arch_user)"
                    "May 13 02:21:22 zenwalk ticky: INFO: Everything fine  [#21111] (buddhist)"]
        expected = []
        self.assertEqual(rank_errors(testcase), expected)
        
    def test_brackets_in_error(self):
        testcase = ["May 27 11:55:40 ubuntu.local ticky: ERROR: Something failed (or broken) absolutely (bad_user)",
                    "Feb 10 09:33:13 ubuntu.remote ticky: ERROR: Little thing broken (asta la vista!) (little_user)",
                    "Jan 24 15:14:24 archlinux ticky: ERROR: Something failed (or broken) absolutely (arch_user)"]
        expected = [("Something failed (or broken) absolutely", 2), ("Little thing broken (asta la vista!)", 1)]
        self.assertEqual(rank_errors(testcase), expected)
        
    def test_test(self):
        testcase = ["May 13 12:44:32 ubuntu ticky: INFO: Everything fine  [#12345] (info_user)",
                    "Sep 9 06:01:02 windows ticky: ERROR: Browser failed again (admin)",
                    "Jul 18 23:04:43 debian ticky: ERROR: Browser failed again (debian_root)",
                    "Nov 5 03:03:32 archlinux ticky: INFO: Everything fine  [#99945] (info_user)",
                    "Aug 1 11:11:33 lunali ticky: ERROR: Something broken (info_user)"]
        expected = [("Browser failed again", 2), ("Something broken", 1)]
        self.assertEqual(rank_errors(testcase), expected)
       
        
class TestSortUsersStat(unittest.TestCase):
    def test_basic(self):
        testcase = ["May 13 12:44:32 ubuntu ticky: INFO: Everything fine  [#12345] (info_user)",
                    "Sep 9 06:01:02 windows ticky: ERROR: Browser failed again (admin)",
                    "Jul 18 23:04:43 debian ticky: ERROR: Browser failed again (debian_root)",
                    "Nov 5 03:03:32 archlinux ticky: INFO: Everything fine  [#99945] (info_user)",
                    "Aug 1 11:11:33 lunali ticky: ERROR: Something broken (info_user)"]
        expected = [["admin", "ERROR:1"], ["debian_root", "ERROR:1"], ["info_user", "ERROR:1", "INFO:2"]]
        self.assertEqual(sort_users_stat(testcase), expected)

        
if __name__ == "__main__":
    unittest.main()
