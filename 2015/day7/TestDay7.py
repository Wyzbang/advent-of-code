#!/usr/bin/env python3
"""
Unit Test for 2015 Day class
"""
import unittest
from utils.loader import load_strings
from day7 import Wiring


class TestDay(unittest.TestCase):

    def test1(self):
        actions = load_strings("example.txt")

        wiring = Wiring(actions)

        self.assertEqual(wiring['d'], 72)
        self.assertEqual(wiring['e'], 507)
        self.assertEqual(wiring['f'], 492)
        self.assertEqual(wiring['g'], 114)
        self.assertEqual(wiring['h'], 65412)
        self.assertEqual(wiring['i'], 65079)
        self.assertEqual(wiring['x'], 123)
        self.assertEqual(wiring['y'], 456)


if __name__ == '__main__':
    unittest.main()
