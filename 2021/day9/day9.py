#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/9
"""
import copy
from utils.init import gen_grid
from utils.loader import load_grid_digits


class Grid:

    def __init__(self, data):
        self.grid = data
        self.width = len(data[0])
        self.height = len(data)

    def __str__(self):
        return "%d" % len(self.grid)

    def adjacent(self, i, j):
        a = []

        if i > 0:
            a.append((i-1, j))
        if i < self.height - 1:
            a.append((i+1, j))
        if j > 0:
            a.append((i, j-1))
        if j < self.width - 1:
            a.append((i, j+1))

        return a

    def find_low(self):
        low = []
        for i, row in enumerate(self.grid):
            for j, height in enumerate(row):

                is_lower = []
                for k, m in self.adjacent(i, j):
                    # mark if this cell is lower than adjacent cells
                    is_lower.append(height < self.grid[k][m])

                if all(is_lower):
                    # this cell is only low if it's lower than all 4 adjacent cells
                    low.append(height)

        return sum(low) + len(low)

    def check(self, processed, basins, current, i, j):
        if processed[i][j]:
            return

        value = self.grid[i][j]
        if value < 9:
            if current is None:
                # new basin detected
                current = len(basins)
                basins.append([value])
            else:
                basins[current].append(value)
            processed[i][j] = True
        else:
            return

        # Recursively walk adjacent
        for k, m in self.adjacent(i, j):
            self.check(processed, basins, current, k, m)

        return

    def find_basins(self):
        current = None
        basins = []
        processed = gen_grid(self.width, self.height, False)
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                self.check(processed, basins, current, i, j)

        sizes = []
        for basin in basins:
            sizes.append(len(basin))
        sizes.sort()
        answer = sizes[-3] * sizes[-2] * sizes[-1]

        return answer


def run():
    print("Advent of Code 2021 - Day 9")
    grid = Grid(load_grid_digits("input.txt"))
    print("PART1: Low   = ", grid.find_low())
    print("PART2: Basin = ", grid.find_basins())


if __name__ == "__main__":
    run()
