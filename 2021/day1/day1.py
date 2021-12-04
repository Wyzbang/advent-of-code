#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/1
"""


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            numbers.append(int(line))

        print("Loaded %s items" % (len(numbers)))
        return numbers


def day1_part1(data):
    increases = 0
    last = data[0]
    for line in data[1:]:
        new = line
        if new > last:
            increases += 1
        last = new
    print("PART1: %d of %s data increased" % (increases, len(data)))


def day1_part2(data):
    increases = 0
    last = sum(data[0:3])

    for i in range(1, len(data)):
        new = sum(data[i:i+3])
        if new > last:
            increases += 1
        last = new
    print("PART2: %d of %s data increased" % (increases, len(data)))


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 1")
    parsed = load()
    day1_part1(parsed)
    day1_part2(parsed)
