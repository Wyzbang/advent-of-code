#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/5
"""


class Vent:
    def __init__(self, value):
        tmp = value.split(" -> ")
        tmp1 = tmp[0].split(',')
        tmp2 = tmp[1].split(',')
        self.x1 = int(tmp1[0])
        self.y1 = int(tmp1[1])
        self.x2 = int(tmp2[0])
        self.y2 = int(tmp2[1])

    def __str__(self):
        return "%d,%d -> %d,%d" % (self.x1, self.y1, self.x2, self.y2)


class Grid:
    def __init__(self, vents, diagonal):
        self.grid = []
        self.diagonal = diagonal
        self.init_grid(vents)
        self.populate_grid(vents)
        self.vents = vents

    def print(self):
        for row in self.grid:
            for value in row:
                print((value if value > 0 else "."), end='')
            print()

    def init_grid(self, vents):
        width = 0
        height = 0
        for vent in vents:
            if vent.x1 > width:
                width = vent.x1
            if vent.x2 > width:
                width = vent.x2
            if vent.y1 > height:
                height = vent.y1
            if vent.y2 > height:
                height = vent.y2

        self.grid = [[0 for i in range(width+1)] for j in range(height+1)]

    def populate_grid(self, vents):
        for vent in vents:

            if vent.x1 == vent.x2:
                #  vertical line
                column = vent.x1
                down = -1 if vent.y1 > vent.y2 else 1
                for row in range(vent.y1, vent.y2 + down, down):
                    self.grid[row][column] += 1

            elif vent.y1 == vent.y2:
                # horizontal Line
                row = vent.y1
                left = -1 if vent.x1 > vent.x2 else 1
                for column in range(vent.x1, vent.x2 + left, left):
                    self.grid[row][column] += 1

            elif self.diagonal:
                # diagonal line (45 degree only)
                down = -1 if vent.y1 > vent.y2 else 1
                left = -1 if vent.x1 > vent.x2 else 1

                # Fix end (range is non-inclusive) and direction
                xs = range(vent.x1, vent.x2 + left, left)
                ys = range(vent.y1, vent.y2 + down, down)

                for i in range(len(xs)):
                    x = xs[i]
                    y = ys[i]
                    self.grid[y][x] += 1


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        vents = []
        # Format read data
        for line in lines:
            vent = Vent(line)
            vents.append(vent)

        return vents


def part(index, data, diagonal):
    grid = Grid(data, diagonal)

    overlap = 0
    for row in grid.grid:
        for value in row:
            if value >= 2:
                overlap += 1

    print("PART%d: Overlapping points %d" % (index, overlap))
    #grid.print()


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 5")
    parsed = load()
    part(1, parsed, False)
    part(2, parsed, True)
