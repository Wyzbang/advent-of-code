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
    def __init__(self, data):
        self.grid = []
        self.init_grid(data)
        self.populate_grid(data)

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
                column = vent.x1
                if vent.y1 > vent.y2:
                    a = vent.y2
                    b = vent.y1
                else:
                    a = vent.y1
                    b = vent.y2

                for row in range(a, b+1):
                    self.grid[row][column] += 1

            if vent.y1 == vent.y2:
                row = vent.y1
                if vent.x1 > vent.x2:
                    a = vent.x2
                    b = vent.x1
                else:
                    a = vent.x1
                    b = vent.x2

                for column in range(a, b+1):
                    self.grid[row][column] += 1


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        vents = []
        # Format read data
        for line in lines:
            vent = Vent(line)
            vents.append(vent)

        return vents


def part1(data):
    grid = Grid(data)

    overlap = 0
    for row in grid.grid:
        for value in row:
            if value >= 2:
                overlap += 1

    print("PART1: Overlapping points", overlap)


def part2(data):

    print("PART2: ")


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 5")
    parsed = load()
    part1(parsed)
    part2(parsed)
