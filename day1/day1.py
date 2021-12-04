#!/usr/bin/env python3

def load():
    with open("input.txt") as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            numbers.append(int(line))

        print("Loaded %s items" % (len(numbers)))
        return numbers


def day1_part1(lines):
    increases = 0
    last = lines[0]
    for line in lines[1:]:
        new = line
        if new > last: increases += 1
        last = new
    print("PART1: %d of %s lines increased" % (increases, len(lines)))


def day1_part2(lines):
    increases = 0
    last = sum(lines[0:3])

    for i in range(1, len(lines)):
        new = sum(lines[i:i+3])
        if new > last: increases += 1
        last = new
    print("PART2: %d of %s lines increased" % (increases, len(lines)))


if __name__ == "__main__":
    print("Avent of Code 2021 - Day 1")
    lines = load()
    day1_part1(lines)
    day1_part2(lines)
