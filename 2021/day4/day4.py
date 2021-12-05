#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/
"""
import os


def transpose(matrix):
    """
    Transpose a matrix (e.g. swap column and rows)
    :param matrix: the matrix to transpose
    :return: the transposed matrix
    """
    width = len(matrix[0])
    height = len(matrix)
    converted = [[0 for i in range(height)] for j in range(width)]

    for c, row in enumerate(matrix):
        if len(row) != width:
            raise RuntimeError("Row sizes do not match")

        for r, item in enumerate(row):
            converted[r][c] = item

    return converted


class BingoCard:

    def __init__(self):
        self.rows = []
        self.matched = []

    def __str__(self):
        formatted = ""
        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                match = "+" if self.matched[i][j] else "-"
                formatted += "%2s%s " % (value, match)
            formatted += os.linesep
        return formatted

    def add_row(self, row):
        if len(row) != 5:
            raise(RuntimeError("Invalid row width: %d" % (len(row))))
        self.rows.append(row)
        self.matched.append([False for i in range(len(row))])

    def mark(self, chosen):
        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                if chosen == value:
                    self.matched[i][j] = True
                    return

    def has_bingo(self):
        for row in self.matched:
            if all(row):
                return True
        for column in transpose(self.matched):
            if all(column):
                return True
        return False

    def score(self, last):
        total = 0
        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                if not self.matched[i][j]:
                    total += int(value)
        total = total * int(last)
        return total


def load():
    with open("input.txt") as file:
        lines = file.readlines()

        # Format read data
        pulls = lines[0].strip().split(',')
        print(pulls)
        cards = []
        for line in lines[1:]:
            if line.strip() == '':
                cards.append(BingoCard())
            else:
                last = len(cards) - 1
                new_row = line.strip().split()
                cards[last].add_row(new_row)

        print("Pulls: %d, Cards: %d" % (len(pulls), len(cards)))
        return pulls, cards


def part1(pulls, cards):
    for card in cards:
        print(card)
    print(pulls)

    winner = None
    score = None
    for pull in pulls:
        for card in cards:
            card.mark(pull)
            won = card.has_bingo()
            if won:
                winner = card
                break
        if winner is not None:
            score = card.score(pull)
            break

    print("PART1: Winner Score:", score)
    print(winner)


def part2(pulls, cards):

    print("PART2: ")


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 4")
    parsed = load()
    part1(*parsed)
    part2(*parsed)
