#!/usr/bin/env python3
"""
Unit Test for 2015 Day class
"""
import unittest
from day3 import Delivery


class TestDay3(unittest.TestCase):
    def __test_delivery(self, directions, expected):
        d = Delivery()
        d.deliver(directions)

        self.assertEqual(expected, d.get_unique())

    def test1(self):
        # Delivers presents to 2 houses: one at the starting location, and one to the east.
        self.__test_delivery(">", 2)

    def test2(self):
        # Delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
        self.__test_delivery("^>v<", 4)

    def test3(self):
        # Delivers a bunch of presents to some very lucky children at only 2 houses.
        self.__test_delivery("^v^v^v^v^v", 2)


if __name__ == '__main__':
    unittest.main()
