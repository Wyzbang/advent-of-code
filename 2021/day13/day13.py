#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/
"""
from utils.converters import split_point
from utils.grid import Grid
from utils.loader import load_lines


class Fold:

    def __init__(self, data):
        self.dir, self.pos = self.parse(data)

    def parse(self, line):
        tmp = line.strip().split()[2].split('=')
        return tmp[0], int(tmp[1])


class Manual:

    def __init__(self, filepath):
        self.points = []
        self.grid = None
        self.folds = []
        self.load(filepath)

    def __str__(self):
        return "Coords: %d, Folds: %d" % (len(self.points), len(self.folds))

    def load(self, filepath):
        lines = load_lines(filepath)
        width = 0
        height = 0
        for line in lines:
            if ',' in line:
                x, y = split_point(line)
                self.points.append((x, y))
                width = x if x > width else width
                height = y if y > height else height
            elif "fold" in line:
                self.folds.append(Fold(line))

        self.grid = Grid.initialize(width+1, height+1, False)
        for x, y in self.points:
            self.grid.set(x, y, True)
        self.grid.dump()

    def has_folds(self):
        return len(self.folds) > 0

    def fold(self):
        action = self.folds.pop(0)
        if action.dir == 'y':
            new_height = self.grid.height - action.pos - 1
            folded = Grid.initialize(self.grid.width, new_height, False)
            # fold up
            fold_height = self.grid.height - action.pos - 1
            r0 = range(0, action.pos - fold_height)
            r1 = list(range(action.pos - fold_height, action.pos))
            r2 = list(range(self.grid.height - 1, action.pos, -1))

            # copy the unaffected rows to result
            for i in r0:
                for j in range(self.grid.width):
                    folded[i][j] = self.grid[i][j]

            # set folded values
            for i in range(fold_height):
                for j in range(self.grid.width):
                    a = r1[i]
                    b = r2[i]
                    folded[a][j] = self.grid[a][j] or self.grid[b][j]

            self.grid = folded

        else:
            new_width = self.grid.width - action.pos - 1
            folded = Grid.initialize(new_width, self.grid.height, False)

            # fold left
            fold_width = self.grid.width - action.pos - 1
            r0 = range(0, action.pos - fold_width)
            r1 = list(range(action.pos - fold_width, action.pos))
            r2 = list(range(self.grid.width - 1, action.pos, -1))

            # copy the unaffected rows to result
            for j in range(self.grid.height):
                for i in r0:
                    folded[i][j] = self.grid[i][j]

            # set folded values
            for j in range(fold_width):
                for i in range(self.grid.height):
                    a = r1[j]
                    b = r2[j]
                    folded[i][a] = self.grid[i][a] or self.grid[i][b]

            self.grid = folded


def run():
    print("Advent of Code 2021 - Day ")
    manual = Manual("input.txt")
    print()
    manual.fold()
    answer1 = manual.grid.count(True)

    while manual.has_folds():
        manual.fold()

    print("PART1: ", answer1)
    print("PART2: ", "HFAJBEHC")
    manual.grid.dump("#", " ")


if __name__ == "__main__":
    run()
