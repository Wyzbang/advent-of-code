#!/usr/bin/env python3
"""
Unit Test for 2015 Day class
"""
import unittest
from day6 import Lights, Action, ActionType


class TestDay(unittest.TestCase):

    def test1(self):
        lights = Lights()
        self.assertEqual(lights.width, 1000)
        self.assertEqual(lights.height, 1000)

    def test2(self):
        a = Action("turn on 489,959 through 759,964")
        self.assertEqual(a.action, ActionType.ON)
        self.assertEqual(a.start, [489, 959])
        self.assertEqual(a.end, [759, 964])

        b = Action("turn off 743,684 through 789,958")
        self.assertEqual(b.action, ActionType.OFF)
        self.assertEqual(b.start, [743, 684])
        self.assertEqual(b.end, [789, 958])

        c = Action("toggle 756,965 through 812,992")
        self.assertEqual(c.action, ActionType.TOGGLE)
        self.assertEqual(c.start, [756, 965])
        self.assertEqual(c.end, [812, 992])


if __name__ == '__main__':
    unittest.main()
