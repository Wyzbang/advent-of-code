#!/usr/bin/env python3
"""
Grid
"""
from utils.converters import split_digits


class Grid:

    def __init__(self):
        self.grid = []
        self.width = None
        self.height = 0

    def __getitem__(self, item):
        return self.grid[item]

    def __str__(self):
        return "Grid (%dx%d)" % (self.width, self.height)

    def initialize(self, width, height, value):
        """
        Generate a grid (list of lists) of size WxH with each cell set to 'value'
        """
        self.grid = [[value for i in range(width)] for j in range(height)]

    def append(self, array):
        size = len(array)
        if self.width is None:
            self.width = size
        elif self.width != size:
            raise RuntimeError("Array size %d does not match current width %d" % (size, self.width))
        self.grid.append(array)
        self.height += 1

    def load_digits(self, filepath):
        with open(filepath) as file:
            lines = file.readlines()
            # Format read data
            for line in lines:
                tmp = split_digits(line.strip())
                self.append(tmp)

    def adjacent_all(self, i, j):
        """
        Find all adjacent cells for a given cell
        :param i:
        :param j:
        :return:
        """
        cells = []

        i1 = i - 1 if i > 0 else 0
        i2 = i + 2 if i < self.height - 1 else self.height
        j1 = j - 1 if j > 0 else 0
        j2 = j + 2 if j < self.width - 1 else self.width

        for k in range(i1, i2):
            for m in range(j1, j2):
                cells.append((k, m))

        # remove this cell
        cells.remove((i, j))
        return cells

    def adjacent(self, i, j):
        """
        Get adjacent cells (non-diagonal)
        :param i:
        :param j:
        :return:
        """
        cells = []

        if i > 0:
            cells.append((i-1, j))
        if i < self.height - 1:
            cells.append((i+1, j))
        if j > 0:
            cells.append((i, j-1))
        if j < self.width - 1:
            cells.append((i, j+1))

        return cells
