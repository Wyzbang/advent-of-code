#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/10
"""
from utils.loader import load_strings


class InvalidLineException(Exception):
    def __init__(self, symbol, score):
        self.symbol = symbol
        self.score = score
        super().__init__("Invalid line found '%s' (score: %d)" % (symbol, score))


class IncompleteLineException(Exception):
    def __init__(self, symbols, score):
        self.symbols = "".join(symbols)
        self.score = score
        super().__init__("Incomplete line needs '%s' (score: %d)" % (symbols, score))


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

    def calc_incomplete_score(self, missing):
        score = 0
        for symbol in missing:
            score = 5 * score
            score += self.scores2[symbol]
        return score

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
                    score = self.scores1[symbol]
                    raise InvalidLineException(symbol, score)

        if len(stack) > 0:
            missing = []
            stack.reverse()
            for symbol in stack:
                missing.append(self.inverse(symbol))

            score = self.calc_incomplete_score(missing)
            raise IncompleteLineException(missing, score)

        return 0


def run():
    print("Advent of Code 2021 - Day 10")
    data = load_strings("input.txt")
    parser = Parser()
    scores1 = []
    scores2 = []
    for line in data:
        try:
            parser.parse(line)
        except InvalidLineException as e1:
            scores1.append(e1.score)

        except IncompleteLineException as e2:
            scores2.append(e2.score)

    # invalid lines total score is sum
    answer1 = sum(scores1)

    # get middle score for incomplete lines
    scores2.sort()
    mid = int((len(scores2) - 1) / 2)
    answer2 = scores2[mid]

    print("PART1: Invalid Lines = ", answer1)
    print("PART2: Incomplete Lines = ", answer2)


if __name__ == "__main__":
    run()
