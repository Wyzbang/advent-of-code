#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/6
"""
import numpy as np


class Fish:
    def __init__(self, counters):
        self.counters = np.array(counters)
        self.days = 0

    def increment(self, days):
        for day in range(days):
            # add number born, after doing decrement
            self.days += 1
            born = 0
            for i, counter in enumerate(self.counters):
                if counter == 0:
                    self.counters[i] = 6
                    born += 1
                else:
                    self.counters[i] = self.counters[i] - 1
            for i in range(born):
                self.counters = np.append(self.counters, 8)
            print("Day %d born %d = %d... " % (self.days, born, len(self.counters)), end="\r")

    def get_total(self):
        return len(self.counters)


def load():
    with open("example.txt") as file:
        lines = file.readlines()

        # Format read data
        counters = []
        for count in lines[0].split(','):
            counters.append(int(count))

        return counters


def run(data):
    fish = Fish(data)
    fish.increment(80)
    print("PART1: Total Lantern Fish", fish.get_total())
    fish.increment(256 - 80)
    print("PART2: Total Lantern Fish", fish.get_total())


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 6")
    parsed = load()
    run(parsed)

