#!/usr/bin/env python3
"""
Unit Test for 2015 Day class
"""
import unittest
from day8 import measure, Parser


class TestDay(unittest.TestCase):

    def test1(self):
        size, length = measure("\"qxfcsmh\"")
        self.assertEqual(size, 9)
        self.assertEqual(length, 7)

    def test2(self):
        size, length = measure("\"qx\\\"fc\"")
        self.assertEqual(size, 8)
        self.assertEqual(length, 5)

    def test3(self):
        size, length = measure("\"ab\\\\cd\"")
        self.assertEqual(size, 8)
        self.assertEqual(length, 5)

    def test4(self):
        size, length = measure("\"ab\\x23cd\"")
        self.assertEqual(size, 10)
        self.assertEqual(length, 5)

    def test5(self):
        values = ["\"\"", "\"abc\"", "\"aaa\\\"aaa\"", "\"\\x27\""]
        parser = Parser(values)
        self.assertEqual(parser.sum, 12)


if __name__ == '__main__':
    unittest.main()
