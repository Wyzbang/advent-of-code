#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/14
"""
from utils.loader import load_lines


class Polymer:

    def __init__(self, filepath):
        self.template = None
        self.rules = []
        self.load(filepath)

    def load(self, filepath):
        data = load_lines(filepath)
        self.template = data[0].strip()
        for rule in data[2:]:
            tmp = tuple(rule.strip().split(" -> "))
            self.rules.append(tmp)

    def insert(self):
        result = self.template[0]
        for i in range(len(self.template) - 1):
            pair = self.template[i:i+2]
            new = None
            for match, insert in self.rules:
                if pair == match:
                    new = insert
                    break
            result += new + pair[1]
        self.template = result

    def counts(self):
        values = {}
        for char in self.template:
            if char not in values:
                values[char] = self.template.count(char)
        return values

    def answer(self):
        counts = self.counts().values()
        return max(counts) - min(counts)


def run():
    print("Advent of Code 2021 - Day 14")
    polymer = Polymer("input.txt")
    for i in range(10):
        polymer.insert()
    answer1 = polymer.answer()

    print("PART1: ", answer1)
    print("PART2: ")


if __name__ == "__main__":
    run()
