#!/usr/bin/env python3
"""
Unit Test for 2015 Day 5 class
"""
import unittest
from day5 import isNice, isNice2


class TestDay(unittest.TestCase):

    def testIsNice(self):
        answer = isNice("ugknbfddgicrmopn")
        self.assertTrue(answer)

        answer = isNice("aaa")
        self.assertTrue(answer)

        answer = isNice("jchzalrnumimnmhp")
        self.assertFalse(answer)

        answer = isNice("haegwjzuvuyypxyu")
        self.assertFalse(answer)

        answer = isNice("dvszwmarrgswjxmb")
        self.assertFalse(answer)

    def testIsNice2(self):
        answer = isNice2("qjhvhtzxzqqjkmpb")
        self.assertTrue(answer)

        answer = isNice2("xxyxx")
        self.assertTrue(answer)

        answer = isNice2("uurcxstgmygtbstg")
        self.assertFalse(answer)

        answer = isNice2("ieodomkazucvgmuy")
        self.assertFalse(answer)


if __name__ == '__main__':
    unittest.main()
