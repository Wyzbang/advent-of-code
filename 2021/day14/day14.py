#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/14
"""
from utils.loader import load_lines


class Counts(dict):

    def __init__(self, *args):
        dict.__init__(self, args)

    def increment(self, key, amount=1):
        if key in self:
            self[key] += amount
        else:
            self[key] = amount


class Polymer:

    def __init__(self, filepath):
        self.template = None
        self.rules = {}
        self.pairs = Counts()
        self.load(filepath)

    def load(self, filepath):
        data = load_lines(filepath)
        self.template = data[0].strip()
        for rule in data[2:]:
            tmp = rule.strip().split(" -> ")
            key = tmp[0]
            value = tmp[1]
            self.rules[key] = value

        for i in range(len(self.template) - 1):
            pair = self.template[i:i+2]
            self.pairs.increment(pair)

    def step(self):
        result = Counts()
        for pair, num in self.pairs.items():
            new = self.rules[pair]
            p1 = pair[0] + new
            result.increment(p1, num)
            p2 = new + pair[1]
            result.increment(p2, num)
        self.pairs = result

    def answer(self):
        counts = Counts()
        for pair, count in self.pairs.items():
            counts.increment(pair[0], count)

        # need to count last letter
        counts.increment(self.template[-1])

        counts2 = counts.values()
        return max(counts2) - min(counts2)


def run():
    print("Advent of Code 2021 - Day 14")
    polymer = Polymer("input.txt")
    for i in range(10):
        polymer.step()
    answer1 = polymer.answer()
    print("PART1: After 10 steps: ", answer1)
    for i in range(30):
        polymer.step()
        print("%d" % i, end="\r")
    answer2 = polymer.answer()

    print("PART2: After 40 steps: ", answer2)


if __name__ == "__main__":
    run()
