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

    def __add__(self, other):
        new = [self.number, other.number]
        return Snail(new)

    def __eq__(self, other):
        return isinstance(other, Snail) and self.number == other.number

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.number

    @staticmethod
    def is_regular(pair):
        return type(pair) is list and type(pair[0]) is int and type(pair[1]) is int

    @staticmethod
    def explode(l, i):
        prev = l[0]
        next = l[1]
        l = 0
        return prev, next


    @staticmethod
    def split(l, i):
        half = l[i] / 2
        a = math.floor(half)
        b = math.ceil(half)

        l[i] = [a, b]

    def explode(self, pairs=None, depth=0):
        pairs = self.number if pairs is None else pairs
        prev_inc = 0
        next_inc = 0
        exploded = 0

        for i, node in enumerate(pairs):
            if i == 1:
                pairs[0] += prev_inc

            if type(node) is int:
                pairs[i] += next_inc
                next_inc = 0

            elif self.is_regular(node) and depth >= 3:
                prev_inc = node[0]
                next_inc = node[1]
                pairs[i] = 0
                exploded += 1

            else:
                prev_inc, next_inc, exploded = self.explode(node, depth+1)

        return prev_inc, next_inc, exploded

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





def load(filepath):
    numbers = []
    lines = load_lines(filepath)
    for line in lines:
        number = Snail(line)
        numbers.append(number)

    return numbers


def run():
    print("Advent of Code 2021 - Day 18")
    numbers = load("input.txt")

    # TODO:
    print("PART1: ")
    print("PART2: ")


if __name__ == "__main__":
    run()
