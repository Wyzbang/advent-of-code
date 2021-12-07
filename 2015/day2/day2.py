#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/2
"""


class Present:
    def __init__(self, size):
        self.dimensions = []
        for i in size.split('x'):
            self.dimensions.append(int(i))
        self.dimensions.sort()

    def sides(self):
        sides = [self.dimensions[0] * self.dimensions[1],
                 self.dimensions[0] * self.dimensions[2],
                 self.dimensions[1] * self.dimensions[2]]
        sides.sort()
        return sides

    def paper(self):
        # start with slack, which is equal to smallest side
        total = self.sides()[0]
        for side in self.sides():
            total += (2 * side)
        return total

    def ribbon(self):
        # Warp is around 2 shortest sides
        wrap = ((self.dimensions[0] * 2) + (self.dimensions[1] * 2))
        # bow amount is volume
        bow = (self.dimensions[0] * self.dimensions[1] * self.dimensions[2])

        return wrap + bow


def load():
    with open("input.txt") as file:
        lines = file.readlines()

        # Format read data
        presents = []
        for line in lines:
            presents.append(Present(line))

        return presents


def run(data):
    paper = 0
    ribbon = 0
    for present in data:
        paper += present.paper()
        ribbon += present.ribbon()

    print("PART1: %d square feet of paper" % paper)
    print("PART2: %d feet of ribbon" % ribbon)


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 2")
    parsed = load()
    run(parsed)
