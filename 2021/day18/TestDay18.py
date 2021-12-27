#!/usr/bin/env python3
"""
Unit Test for Day 17 class
"""
import unittest
from day18 import Snail


class TestDay18(unittest.TestCase):

    def __test_sum(self, a, b, exp):
        sa = Snail(a)
        sb = Snail(b)

        actual = sa + sb
        expected = Snail(exp)
        self.assertEqual(expected, actual)

    def test_sum1(self):
        self.__test_sum([1,2], [[3, 4], 5], [[1,2],[[3,4],5]])

    def test_sum2(self):
        self.__test_sum([[[[4,3],4],4],[7,[[8,4],9]]], [1,1], [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])

    def __test_explode(self, before, after):
        actual = Snail(before)
        expected = Snail(after)

        actual.explode()
        self.assertEqual(expected, actual)

    def test_explode1(self):
        a = [[[[[9,8],1],2],3],4]
        b = [[[[0,9],2],3],4]
        self.__test_explode(a, b)

    def test_explode2(self):
        a = [7,[6,[5,[4,[3,2]]]]]
        b = [7,[6,[5,[7,0]]]]
        self.__test_explode(a, b)

    def test_explode3(self):
        a = [[6,[5,[4,[3,2]]]],1]
        b = [[6,[5,[7,0]]],3]
        self.__test_explode(a, b)

    def test_explode4(self):
        a = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
        b = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        self.__test_explode(a, b)

    def test_explode5(self):
        a = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        b = [[3,[2,[8,0]]],[9,[5,[7,0]]]]
        self.__test_explode(a, b)

    def __test_split(self, before, after):
        actual = Snail(before)
        expected = Snail(after)

        was_split = actual.split()
        self.assertEqual(expected, actual)
        return was_split

    def test_split1(self):
        a = [[[[0,7],4],[15,[0,13]]],[1,1]]
        b = [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
        was_split = self.__test_split(a, b)
        self.assertTrue(was_split)

    def test_split2(self):
        a = [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
        b = [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
        was_split = self.__test_split(a, b)
        self.assertTrue(was_split)

    def test_split_not_needed(self):
        a = [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
        was_split = self.__test_split(a, a)
        self.assertFalse(was_split)


if __name__ == '__main__':
    unittest.main()