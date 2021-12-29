#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/18
"""
import math
from utils.loader import load_lines


class Snail:
    """
    Snailfish Number
    """
    def __init__(self, number):
        if type(number) is str:
            self.number = eval(number)
        elif type(number) is list:
            self.number = number
        else:
            raise RuntimeError

        self.exploded = False
        self.next_inc = 0
        self.prev_inc = 0

    def __add__(self, other):
        new = [self.number, other.number]
        return Snail(new)

    def __eq__(self, other):
        return isinstance(other, Snail) and self.number == other.number

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.number.__str__()

    @staticmethod
    def is_regular(pair):
        return type(pair) is list and type(pair[0]) is int and type(pair[1]) is int

    def explode(self):
        self.exploded = False
        self.next_inc = 0
        self.prev_inc = 0
        self.__explode(self.number)
        return self.exploded

    def __explode(self, pairs=None, depth=0):

        for i, pair in enumerate(pairs):

            if type(pair) is list and type(pair[0]) is int:
                pair[0] += self.next_inc
                self.next_inc = 0

            if type(pair) is int:
                pass

            elif not self.exploded and self.is_regular(pair) and depth >= 3:
                # if this is first of the pair, increment the next and return prev
                # or vice-versa
                self.exploded = True
                self.prev_inc = pair[0]
                self.next_inc = pair[1]
                pairs[i] = 0

                if i == 0:
                    if type(pairs[1]) is int:
                        pairs[1] += self.next_inc
                        self.next_inc = 0
                    elif type(pairs[1][0]) is int:
                        pairs[1][0] += self.next_inc
                        self.next_inc = 0
                else:
                    if type(pairs[0]) is int:
                        pairs[0] += self.prev_inc
                        self.prev_inc = 0
                    elif type(pairs[0][0]) is int:
                        pairs[0][0] += self.prev_inc
                        self.prev_inc = 0

                return

            else:
                self.__explode(pair, depth+1)
                if self.exploded and self.next_inc == 0 and self.prev_inc == 0:
                    return

            if i == 1:
                if type(pairs[0]) is int:
                    pairs[0] += self.prev_inc
                    self.prev_inc = 0

            elif i == 0:
                if type(pairs[1]) is int:
                    pairs[1] += self.next_inc
                    self.next_inc = 0

            if depth == 1:
                # if get to top and there is no previous, drop value
                self.prev_inc = 0

        return

    def split(self, pairs=None):
        pairs = self.number if pairs is None else pairs
        for i, pair in enumerate(pairs):
            if type(pair) is int and pair > 9:
                first = math.floor(pair / 2)
                second = math.ceil(pair / 2)
                pairs[i] = [first, second]
                return True
            elif type(pair) is list:
                done = self.split(pair)
                if done:
                    return True

        return False

    def reduce(self):
        needs_explode = True
        needs_split = True
        print("START  :", self.number)
        while needs_explode or needs_split:
            exploded = self.explode()
            needs_explode = exploded
            if exploded:
                print("EXP    :", self.number)
                needs_split = True
            elif needs_split:
                was_split = self.split()
                needs_split = was_split
                if was_split:
                    print("SPLIT  :", self.number)
                    needs_explode = True

    def magnitude(self, pairs=None):
        pairs = self.number if pairs is None else pairs
        mag = 0
        if self.is_regular(pairs):
            return 3*pairs[0] + 2*pairs[1]
        elif type(pairs) is list:
            for i, pair in enumerate(pairs):
                mag += self.magnitude(pair)

        return self.magnitude(pairs)


def load(filepath):
    numbers = []
    lines = load_lines(filepath)
    for line in lines:
        number = Snail(line)
        numbers.append(number)

    return numbers


def part1(numbers):
    current = numbers[0]
    print("cur", 0, current)
    for i, number in enumerate(numbers[1:]):
        current += number
        print("sum", i, current)
        current.reduce()
        print("red", i, current)

    answer = current.magnitude()
    return answer


def run():
    print("Advent of Code 2021 - Day 18")
    numbers = load("sum_example.txt")

    # TODO:
    answer1 = part1(numbers)

    print("PART1: ", answer1)
    print("PART2: ")


if __name__ == "__main__":
    run()
