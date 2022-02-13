#!/usr/bin/env python3
"""
Unit Test for 2015 Day class
"""
import unittest
from day4 import find_hash


class TestDay3(unittest.TestCase):

    def __test_find(self, prefix, expected):
        answer = "%s%d" % (prefix, expected)
        key, hash = find_hash(prefix, expected - 10)
        self.assertEqual(key, answer)

    def test1(self):
        self.__test_find("abcdef", 609043)

    def test2(self):
        self.__test_find("pqrstuv", 1048970)


if __name__ == '__main__':
    unittest.main()
