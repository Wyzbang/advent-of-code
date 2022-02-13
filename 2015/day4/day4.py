#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/
"""
import hashlib
from utils.progress import Spinner


def find_hash(prefix, start=1, zeros=5):
    spinner = Spinner(1000)
    suffix = start
    match = "0" * zeros
    while True:
        key = "%s%d" % (prefix, suffix)
        md5 = hashlib.md5(key.encode())
        hex = md5.hexdigest()[0:zeros]
        if hex == match:
            return key

        suffix += 1
        spinner.display(suffix)


def run():
    print("Advent of Code 2015 - Day 4")
    # TODO:
    key1 = find_hash("iwrupvqb")

    print("PART1: ", key1)

    key2 = find_hash("iwrupvqb", zeros=6)
    print("PART2: ", key2)


if __name__ == "__main__":
    run()
