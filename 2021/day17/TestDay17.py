#!/usr/bin/env python3
"""
Unit Test for Day 17 class
"""
import unittest
from day17 import Target, Probe


class TestDay17(unittest.TestCase):

    def setUp(self):
        pass

    def test_target(self):
        t1 = Target(10, 20, -20, -10)
        self.assertTrue(t1.hit(10, -10))
        self.assertTrue(t1.hit(20, -20))
        self.assertTrue(t1.hit(15, -15))

        self.assertFalse(t1.hit(0, 0))
        self.assertFalse(t1.hit(21, -21))
        self.assertFalse(t1.hit(20, -21))
        self.assertFalse(t1.hit(21, -20))

    def test_probe(self):
        p1 = Probe(0, 0)
        p1.step()
        self.assertEqual(p1.location, (0, 0))
        p1.step()
        self.assertEqual(p1.location, (0, -1))
        p1.step()
        self.assertEqual(p1.location, (0, -3))

    def __hit_after(self, vx, vy, n):
        example = Target(20, 30, -10, -5)
        probe = Probe(vx, vy)
        for i in range(n):
            self.assertFalse(example.hit(*probe.location), "before step %d" % i)
            probe.step()
        self.assertTrue(example.hit(*probe.location))

    def test_example1(self):
        self.__hit_after(7, 2, 7)

    def test_example2(self):
        self.__hit_after(6, 3, 9)

    def test_example3(self):
        self.__hit_after(9, 0, 4)

    def test_example4(self):
        example = Target(20, 30, -10, -5)
        probe = Probe(17, -4)
        for i in range(4):
            probe.step()
            self.assertFalse(example.hit(*probe.location), "after step %d" % i)

    def __highest1(self, vx, vy, n):
        example = Target(20, 30, -10, -5)
        probe = Probe(vx, vy)
        hit, highest = probe.find_highest(example)

        self.assertEqual(n, highest)
        self.assertTrue(hit)

    def test_highest1(self):
        self.__highest1(7, 2, 3)

    def test_highest2(self):
        self.__highest1(6, 3, 6)

    def test_highest3(self):
        self.__highest1(9, 0, 0)

    def test_highest4(self):
        example = Target(20, 30, -10, -5)
        probe = Probe(17, -4)
        hit, highest = probe.find_highest(example)

        self.assertEqual(0, highest)
        self.assertFalse(hit)

    def test_highest5(self):
        self.__highest1(6, 9, 45)


if __name__ == '__main__':
    unittest.main()