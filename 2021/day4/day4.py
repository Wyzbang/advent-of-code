#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/
"""
import itertools
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

    def __init__(self, index):
        self.rows = []
        self.matched = []
        self.index = index

    def __str__(self):
        formatted = "===== Card %2d =====" % self.index
        formatted += os.linesep
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
        cards = []
        for line in lines[1:]:
            if line.strip() == '':
                cards.append(BingoCard(len(cards)))
            else:
                last = len(cards) - 1
                new_row = line.strip().split()
                cards[last].add_row(new_row)

        print("Pulls: %d, Cards: %d" % (len(pulls), len(cards)))
        return pulls, cards


def part1(pulls, cards):
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

    print(winner)
    print("PART1: Winner Score:", score)


def filter_bingo(card):
    return card.has_bingo()


def part2(pulls, cards):
    """
    NOTE: The first winner was already determined in PART 1, so some pulls are already marked
    :param pulls:
    :param cards:
    :return:
    """
    remaining = list(cards)
    for i, pull in enumerate(pulls):
        for card in remaining:
            card.mark(pull)

        # Filter list to only bingo cards that have not won
        remaining[:] = itertools.filterfalse(filter_bingo, remaining)
        if len(remaining) == 1:
            # continue until the last card "wins"
            loser = remaining[0]
            for pull2 in pulls[i:]:
                loser.mark(pull2)
                if loser.has_bingo():
                    score = loser.score(pull2)
                    print(loser)
                    print("PART2: Loser Score:", score)
                    return


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 4")
    parsed = load()
    part1(*parsed)
    part2(*parsed)
