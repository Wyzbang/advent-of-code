#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/1
"""


def load():
    with open("input.txt") as file:
        lines = file.readlines()

        # Format read data

        return lines


def part1(data):
    floor = 0
    for value in data[0]:
        if value == "(":
            floor += 1
        elif value == ")":
            floor -= 1

    print("PART1: Leave present on floor ", floor)


def part2(data):
    floor = 0
    answer = None
    for i, value in enumerate(data[0]):
        if value == "(":
            floor += 1
        elif value == ")":
            floor -= 1

        if floor == -1:
            # The index is 1 based, per rules
            answer = i + 1
            break

    print("PART2: First Basement index ", answer)


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 1")
    parsed = load()
    part1(parsed)
    part2(parsed)
