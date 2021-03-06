#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/18
"""
import logging
import math
from utils.loader import load_lines

logging.basicConfig(level=logging.WARN, format="%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Snail:
    """
    Snailfish Number
    """
    def __init__(self, number):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

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

    def increment(self, indexes, amount):
        tmp = self.number
        for index in indexes[:-1]:
            tmp = tmp[index]

        tmp[indexes[-1]] += amount

    @staticmethod
    def is_regular(pair):
        return type(pair) is list and type(pair[0]) is int and type(pair[1]) is int

    def explode(self):
        self.exploded = False
        self.next_inc = 0
        self.prev_inc = 0
        self.prev = None
        self.__explode(self.number)
        return self.exploded

    def __explode(self, pairs=None, depth=0, path=[]):

        for i, pair in enumerate(pairs):

            if type(pair) is list and type(pair[i]) is int:
                pair[i] += self.next_inc
                self.next_inc = 0

            if type(pair) is int:
                self.prev = path + [i]

            elif not self.exploded and self.is_regular(pair) and depth >= 3:
                # if this is first of the pair, increment the next and return prev
                # or vice-versa
                self.exploded = True
                prev_inc = pair[0]
                self.next_inc = pair[1]
                pairs[i] = 0

                if self.prev is not None:
                    self.increment(self.prev, prev_inc)

                if i == 0:
                    if type(pairs[1]) is int:
                        pairs[1] += self.next_inc
                        self.next_inc = 0

            else:
                self.__explode(pair, depth+1, path + [i])
                """
                if type(pair) is list and type(pair[1]) is int:
                    pair[1] += self.next_inc
                    self.next_inc = 0
                """
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
        self.logger.debug("START  : %s", self.number)
        while needs_explode or needs_split:
            exploded = self.explode()
            needs_explode = exploded
            if exploded:
                self.logger.debug("EXP    : %s", self.number)
                needs_split = True
            elif needs_split:
                was_split = self.split()
                needs_split = was_split
                if was_split:
                    self.logger.debug("SPLIT  : %s", self.number)
                    needs_explode = True

    def magnitude(self, pairs=None):
        return self.__magnitude(self.number)

    def __magnitude(self, items):
        tmp = [0, 0]
        for i, item in enumerate(items):
            multi = 3 if i == 0 else 2
            if type(item) is int:
                tmp[i] = multi * item
            else:
                tmp[i] = multi * self.__magnitude(item)

        return sum(tmp)


def load(filepath):
    numbers = []
    lines = load_lines(filepath)
    for line in lines:
        number = Snail(line)
        numbers.append(number)

    return numbers


def part1(numbers):
    current = numbers[0]
    logger.debug("CUR: %d %s", 0, current)
    for i, number in enumerate(numbers[1:]):
        current += number
        logger.debug("SUM: %d %s", i, current)
        current.reduce()
        logger.debug("RED: %d %s", i, current)

    answer = current.magnitude()
    return answer


def run():
    logger.info("Advent of Code 2021 - Day 18")
    numbers = load("sum_example.txt")

    # TODO:
    answer1 = part1(numbers)

    logger.info("PART1: %d", answer1)
    logger.info("PART2: ")


if __name__ == "__main__":
    run()
