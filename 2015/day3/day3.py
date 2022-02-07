#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/
"""
from utils.loader import load_chars


class Delivery:

    def __init__(self):
        self.location = (0, 0)
        self.location2 = (0, 0)
        self.delivered = {self.location: 1}

    def get_unique(self):
        return len(self.delivered)

    def increment(self, location):
        if location in self.delivered:
            self.delivered[location] += 1
        else:
            self.delivered[location] = 1

    def move(self, which, direction):
        """
        # north (^), south (v), east (>), or west (<).
        """
        n, e = self.location if which == 0 else self.location2
        if direction == '^':
            n += 1
        elif direction == 'v':
            n -= 1
        elif direction == '>':
            e += 1
        elif direction == '<':
            e -= 1

        if which == 0:
            self.location = (n,e)
            self.increment(self.location)
        else:
            self.location2 = (n,e)
            self.increment(self.location2)

    def deliver(self, directions):

        for direction in directions:
            self.move(0, direction)

    def deliver2(self, directions):

        for i, direction in enumerate(directions):
            which = i % 2
            self.move(which, direction)
            self.increment(self.location)



def run():
    print("Advent of Code 2015 - Day 3")
    directions = load_chars("input.txt")

    # TODO:
    d = Delivery()
    d.deliver(directions)

    print("PART1: ", d.get_unique())

    d2 = Delivery()
    d2.deliver2(directions)
    print("PART2: ", d2.get_unique())


if __name__ == "__main__":
    run()
