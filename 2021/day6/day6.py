#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/6
"""


class Fish:
    """
    Fish is an array of the number of fish currently at that counter level
    """

    def __init__(self, initial):
        self.days = 0
        self.fish = [0 for i in range(9)]
        for value in initial:
            self.fish[value] += 1

    def increment(self, days):
        for day in range(days):
            self.days += 1

            # Store the number of fish at 0 (will goto to 6 and spawn new fish at 8)
            zeros = self.fish[0]
            for i in range(8):
                self.fish[i] = self.fish[i+1]
            self.fish[6] += zeros
            self.fish[8] = zeros

            print("Day %d born %d = %d... " % (self.days, zeros, self.total()), end="\r")

    def total(self):
        return sum(self.fish)


def load():
    with open("input.txt") as file:
        lines = file.readlines()

        # Format read data
        counters = []
        for count in lines[0].split(','):
            counters.append(int(count))

        return counters


def run(data):
    fish = Fish(data)
    fish.increment(80)
    print("PART1: Lantern Fish after  80:", fish.total())
    fish.increment(256 - 80)
    print("PART2: Lantern Fish after 256:", fish.total())


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 6")
    parsed = load()
    run(parsed)

