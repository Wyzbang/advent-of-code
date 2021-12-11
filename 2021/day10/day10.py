#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/10
"""
from utils.loader import load_strings


class Parser:
    opener = ['(', '[', '{', '<']
    closer = [')', ']', '}', '>']

    scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    scores2 = {')': 1, ']': 2, '}': 3, '>': 4}

    def inverse(self, symbol):
        if symbol in self.closer:
            i = self.closer.index(symbol)
            return self.opener[i]
        else:
            i = self.opener.index(symbol)
            return self.closer[i]

    def parse(self, line):
        stack = []
        for symbol in line:
            if symbol in self.opener:
                stack.append(symbol)
            else:
                last = len(stack) - 1
                if stack[last] == self.inverse(symbol):
                    stack.pop()
                else:
                    # corrupt data
                    return self.scores1[symbol]

        return 0


def run():
    print("Advent of Code 2021 - Day 10")
    data = load_strings("input.txt")
    parser = Parser()
    score = 0
    for line in data:
        score += parser.parse(line)
    print("PART1: ", score)
    print("PART2: ")


if __name__ == "__main__":
    run()
