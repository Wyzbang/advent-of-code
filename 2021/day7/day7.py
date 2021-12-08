#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/7
"""

stored = {}

def consumption(delta):
    """
    pre-unit: 1,2,3,4,5
    total:    1,3,6,10,15
    cache result
    """
    if delta in stored:
        return stored[delta]
    used = 0
    for i in range(delta):
        used += (i + 1)
    stored[delta] = used
    return used


class Carbs:

    def __init__(self, positions):
        self.positions = positions

    def max(self):
        return max(self.positions)

    def calculate(self, end):
        fuel = 0
        for position in self.positions:
            if end > position:
                fuel += end - position
            else:
                fuel += position - end
        return fuel

    def calculate2(self, end):
        fuel = 0
        for position in self.positions:
            if end > position:
                delta = end - position
                fuel += consumption(delta)
            else:
                delta = position - end
                fuel += consumption(delta)
        return fuel


def load(filename):
    with open(filename) as file:
        lines = file.readlines()

        # Format read data
        positions = [int(x) for x in lines[0].split(',')]
        return positions


def run(data):
    carbs = Carbs(data)
    fuel1 = None
    fuel2 = None
    final1 = None
    final2 = None
    for end in range(carbs.max() + 1):
        required1 = carbs.calculate(end)
        if fuel1 is None or fuel1 > required1:
            fuel1 = required1
            final1 = end

        required2 = carbs.calculate2(end)
        if fuel2 is None or fuel2 > required2:
            fuel2 = required2
            final2 = end

        print(end, required1, required2)

    print("PART1: Moved to pos %s using %d" % (final1, fuel1))
    print("PART2: Moved to pos %s using %d" % (final2, fuel2))


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 7")
    parsed = load("input.txt")
    run(parsed)
