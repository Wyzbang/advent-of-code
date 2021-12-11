#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/11
"""
from utils.grid import Grid


class Day11Grid(Grid):

    def __init__(self, filepath):
        super().__init__()
        self.load_digits(filepath)
        self.has_flashed = []     # This step only
        self.flashes = 0
        self.steps = 0

    def all_flashed(self):
        """
        Did all octopi flashed on the last step
        """
        return len(self.has_flashed) == (self.width * self.height)

    def step(self):
        self.has_flashed = []
        self.steps += 1

        for i in range(self.width):
            for j in range(self.width):
                self.grid[i][j] += 1

        for i in range(self.width):
            for j in range(self.width):
                if self.grid[i][j] > 9:
                    self.flash(i, j)

        for i, j in self.has_flashed:
            self.grid[i][j] = 0

    def flash(self, i, j):
        if (i, j) in self.has_flashed:
            return

        self.flashes += 1
        self.has_flashed.append((i, j))
        cells = self.adjacent_all(i, j)
        # increment each, check for flash
        for m, n in cells:
            self.grid[m][n] += 1
            if self.grid[m][n] > 9:
                self.flash(m, n)


def run():
    print("Advent of Code 2021 - Day 11")
    grid = Day11Grid("input.txt")

    for i in range(100):
        grid.step()
    answer1 = grid.flashes

    while not grid.all_flashed():
        grid.step()
    answer2 = grid.steps

    print("PART1: Flashes after Step 100 =", answer1)
    print("PART2: All flashed on Step ", answer2)


if __name__ == "__main__":
    run()
