#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/2
"""


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        movements = []
        for line in lines:
            tmp = line.split(' ')
            direction = tmp[0]
            amount = int(tmp[1])
            movements.append({'dir': direction, 'amount': amount})

        print("Loaded %s items" % (len(movements)))
        return movements


def day2_part1(movements):
    depth = 0
    horizontal = 0
    for movement in movements:
        if movement['dir'] == 'forward':
            horizontal += movement['amount']
        elif movement['dir'] == 'up':
            depth -= movement['amount']
        elif movement['dir'] == 'down':
            depth += movement['amount']
        else:
            print("ERROR: Unexpected direction ", movement)

    # Answer is Horizontal * Depth
    answer = horizontal * depth
    print("PART1: Horizontal: %d * Depth: %d => %d" % (horizontal, depth, answer))


def day2_part2(movements):
    aim = 0
    depth = 0
    horizontal = 0
    for movement in movements:
        if movement['dir'] == 'forward':
            horizontal += movement['amount']
            depth += aim * movement['amount']
        elif movement['dir'] == 'up':
            aim -= movement['amount']
        elif movement['dir'] == 'down':
            aim += movement['amount']
        else:
            print("ERROR: Unexpected direction ", movement)

    # Answer is Horizontal * Depth
    answer = horizontal * depth
    print("PART2: Horizontal: %d * Depth: %d => %d" % (horizontal, depth, answer))


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 2")
    parsed = load()
    day2_part1(parsed)
    day2_part2(parsed)
