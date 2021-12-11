#!/usr/bin/env python3
"""
Unit Test for Grid class
"""
import unittest
from utils.grid import Grid


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.load = Grid.load_digits("testdata.txt")
        self.init = Grid.initialize(5, 9, False)

    def test_grid_initialize(self):
        self.assertEqual(5, self.init.width)
        self.assertEqual(9, self.init.height)

        # check misc. cells
        self.assertEqual(False, self.init[0][0])
        self.assertEqual(False, self.init[5][3])
        self.assertEqual(False, self.init[8][4])

    def test_grid_load(self):
        self.assertEqual(10, self.load.width)
        self.assertEqual(10, self.load.height)

        # check misc. cells
        self.assertEqual(5, self.load[0][0])
        self.assertEqual(4, self.load[5][5])
        self.assertEqual(6, self.load[9][9])

    def test_adjacent_all_mid(self):
        a = self.load.adjacent_all(5, 5)
        self.assertEqual(8, len(a))
        self.assertTrue((4, 4) in a)
        self.assertTrue((4, 5) in a)
        self.assertTrue((4, 6) in a)
        self.assertTrue((5, 4) in a)
        self.assertTrue((5, 6) in a)
        self.assertTrue((6, 4) in a)
        self.assertTrue((6, 5) in a)
        self.assertTrue((6, 6) in a)

    def test_adjacent_all_tl(self):
        a = self.load.adjacent_all(0, 0)
        self.assertEqual(3, len(a))
        self.assertTrue((0, 1) in a)
        self.assertTrue((1, 1) in a)
        self.assertTrue((1, 0) in a)

    def test_adjacent_all_br(self):
        a = self.load.adjacent_all(9, 9)
        self.assertEqual(3, len(a))
        self.assertTrue((8, 8) in a)
        self.assertTrue((8, 9) in a)
        self.assertTrue((9, 8) in a)

    def test_adjacent_mid(self):
        a = self.load.adjacent(5, 5)
        self.assertEqual(4, len(a))
        self.assertTrue((4, 5) in a)
        self.assertTrue((5, 4) in a)
        self.assertTrue((5, 6) in a)
        self.assertTrue((6, 5) in a)

    def test_adjacent_tl(self):
        a = self.load.adjacent(0, 0)
        self.assertEqual(2, len(a))
        self.assertTrue((0, 1) in a)
        self.assertTrue((1, 0) in a)

    def test_adjacent_br(self):
        a = self.load.adjacent(9, 9)
        self.assertEqual(2, len(a))
        self.assertTrue((8, 9) in a)
        self.assertTrue((9, 8) in a)


if __name__ == '__main__':
    unittest.main()
