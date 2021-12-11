#!/usr/bin/env python3
"""
Grid
"""
from utils.converters import split_digits


class Grid:

    def __init__(self, data):
        self.grid = data
        self.width = len(data[0])
        self.height = len(data)

        for row in data:
            if len(row) != self.width:
                raise RuntimeError("Array size %d does not match current width %d" % (len(row), self.width))

    @classmethod
    def initialize(cls, width, height, value):
        data = [[value for i in range(width)] for j in range(height)]
        return cls(data)

    @classmethod
    def load_digits(cls, filepath):
        with open(filepath) as file:
            lines = file.readlines()
            # Format read data
            digits = []
            for line in lines:
                tmp = split_digits(line.strip())
                digits.append(tmp)

            return cls(digits)

    def __getitem__(self, item):
        return self.grid[item]

    def __str__(self):
        return "Grid (%dx%d)" % (self.width, self.height)

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
