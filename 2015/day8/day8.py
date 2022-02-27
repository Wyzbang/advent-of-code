#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/8
"""
from loader import load_strings


def measure(item):
    size = len(item)
    length = 0

    i = 1
    while i < size - 1:
        if item[i] == '\\':
            if item[i+1] in ['"', '\\']:
                length += 1
                i += 2
            elif item[i+1] == "x":
                length += 1
                i += 4
        else:
            length += 1
            i += 1

    return size, length


class Parser:

    def __init__(self, items):
        self.sum = 0
        for item in items:
            size, length = measure(item)
            self.sum += (size - length)


def run():
    print("Advent of Code 2015 - Day 8")
    # TODO:
    strings = load_strings("input.txt")
    parser = Parser(strings)


    print("PART1: ", parser.sum)
    print("PART2: ")


if __name__ == "__main__":
    run()
