#!/usr/bin/env python3
"""
Unit Test for Day 17 class
"""
import unittest
from day18 import Snail


class TestDay18(unittest.TestCase):
    def __test_increment(self, a, indexes, amount, b):
        sa = Snail(a)
        sa.increment(indexes, amount)
        expected = Snail(b)
        self.assertEqual(expected, sa)

    def test_increment1(self):
        a = [[1,2],3]
        indexes = [0,0]
        amount = 1
        b = [[2,2],3]

        self.__test_increment(a,indexes,amount,b)

    def test_increment2(self):
        a = [[1,2],3]
        indexes = [0,1]
        amount = 1
        b = [[1,3],3]

        self.__test_increment(a,indexes,amount,b)

    def test_increment3(self):
        a = [[1,2],3]
        indexes = [1]
        amount = 1
        b = [[1,2],4]

        self.__test_increment(a,indexes,amount,b)

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

        print("START  :", actual)
        actual.explode()
        print("EXPLODE:", actual)
        print("EXPECT :", expected)
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

    def test_explode6(self):
        a = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
        b = [[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]
        self.__test_explode(a,b)

    def __test_split(self, before, after):
        actual = Snail(before)
        expected = Snail(after)

        was_split = actual.split()
        print("EXPECT :", expected)
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

    def __test_reduce(self, before, after):
        actual = Snail(before)
        expected = Snail(after)

        actual.reduce()
        print("EXPECT :", expected)
        self.assertEqual(expected, actual)

    def test_reduce(self):
        a = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
        b = [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
        self.__test_reduce(a, b)

    def test_reduce2(self):
        a = [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]]
        b = [[[[3,0],[6,3]],[4,4]],[5,5]]
        self.__test_reduce(a, b)

    def test_reduce3(self):
        # [[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]] + [6,6]
        a = [[[[0, [5, 3]], [4, 4]], [5, 5]], [6, 6]]
        b = [[[[5,0],[7,4]],[5,5]],[6,6]]
        self.__test_reduce(a, b)

    def test_reduce4(self):
        a = [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
        b = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
        self.__test_reduce(a, b)

    def __test_mag(self, a, expected):
        snail = Snail(a)
        mag = snail.magnitude()
        self.assertEqual(expected, mag)

    def test_magnitude1(self):
        self.__test_mag([1,9], 21)

    def test_magnitude2(self):
        self.__test_mag([[9,1],[1,9]], 129)

    def test_magnitude3(self):
        self.__test_mag([[1,2],[[3,4],5]], 143)

    def test_magnitude3(self):
        self.__test_mag([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384)

    def test_magnitude4(self):
        self.__test_mag([[[[1,1],[2,2]],[3,3]],[4,4]], 445)

    def test_magnitude5(self):
        self.__test_mag([[[[3,0],[5,3]],[4,4]],[5,5]], 791)

    def test_magnitude6(self):
        self.__test_mag([[[[5,0],[7,4]],[5,5]],[6,6]], 1137)

    def test_magnitude7(self):
        self.__test_mag([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488)

    def test_magnitude8(self):
        self.__test_mag([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140)


if __name__ == '__main__':
    unittest.main()
