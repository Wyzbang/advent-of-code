#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/15
"""
import copy
import sys
import time

from utils.grid import Grid


def increment(value, j):
    amount = (j + 1) + value
    value = amount if amount <= 9 else amount - 9
    return value


class Risk(Grid):

    def __init__(self, data):
        super(Risk, self).__init__(data)

        # Recursive
        self.shortest_len  = None
        self.shortest_path = None

        # Dijkstra
        self.unvisited = []
        self.unvisited_scored = []
        self.scores = Grid.initialize(self.width, self.height, sys.maxsize)

        # Performance
        self._start = 0

    def start(self):
        self._start = time.perf_counter()

    def elapsed(self):
        elapsed = time.perf_counter() - self._start
        return "%0.3fs" % elapsed

    def find(self, i, j, path, score):
        print("%d" % (self.shortest_len if self.shortest_len is not None else 0), end='\r')
        new_path = copy.copy(path)
        new_path.append((i, j))
        if self.shortest_len is not None and score > self.shortest_len:
            # stop as this path is higher
            return
        if (i, j) == self.max():
            # Save path and score
            self.shortest_len  = score
            self.shortest_path = new_path
        else:
            for m, n in self.adjacent(i, j):
                if (m, n) not in path:
                    new_score = score + self.grid[m][n]
                    self.find(m, n, new_path, new_score)

    def find_path(self):
        """
        Recursive path finder,
        """
        self.find(0, 0, [], 0)
        return self.shortest_len, self.shortest_path

    def unvisited_adjacent(self, i, j):
        nodes = []
        for node in self.adjacent(i, j):
            if node in self.unvisited:
                nodes.append(node)
        return nodes

    def find_lowest(self):
        lowest = sys.maxsize
        node = self.unvisited[0]
        for i, j in self.unvisited_scored:
            if self.scores[i][j] < lowest:
                lowest = self.scores[i][j]
                node = (i, j)
        return node

    def score(self, i, j, score):
        self.scores[i][j] = score
        node = (i, j)
        if node not in self.unvisited_scored:
            self.unvisited_scored.append(node)

    def mark_visited(self, i, j):
        self.unvisited_scored.remove((i, j))
        self.unvisited.remove((i, j))

    def visit(self, i, j):
        print("Remaining %d (%s)..." % (len(self.unvisited), self.elapsed()), end='\r')
        for n, m in self.unvisited_adjacent(i, j):
            new_score = self.scores[i][j] + self[n][m]
            if new_score < self.scores[n][m]:
                self.score(n, m, new_score)
        self.mark_visited(i, j)

    def dijkstra(self):
        """
        Using Dijkstra's algorithm to find path
        :return:
        """
        self.unvisited = []

        # secondary list of partially scored but unvisited nodes, to speed up algorithm
        # so not evey node needs to be checked for "lowest" for next visit
        self.unvisited_scored = []

        self.scores = Grid.initialize(self.width, self.height, sys.maxsize)

        for i in range(self.height):
            for j in range(self.width):
                self.unvisited.append((i, j))

        # Initialize first node score
        tic = time.perf_counter()
        self.score(0, 0, 0)
        while len(self.unvisited):
            lowest = self.find_lowest()
            self.visit(*lowest)

        toc = time.perf_counter()
        print("Dijkstra completed in %s" % (self.elapsed()))
        f, g = self.max()
        return self.scores[f][g]

    def expand(self):
        # widen
        for i, row in enumerate(self.grid):
            new_row = copy.copy(self.grid[i])
            for j in range(4):
                for value in row:
                    new_value = increment(value, j)
                    new_row.append(new_value)
            self.grid[i] = new_row

        # heighten
        new_rows = []
        for i in range(4):
            for j, row in enumerate(self.grid):
                new_row = []
                for value in row:
                    new_row.append(increment(value, i))
                new_rows.append(new_row)
        self.grid.extend(new_rows)


def run():
    print("Advent of Code 2021 - Day 15")
    risk = Risk.load_digits("input.txt")

    #score, path = risk.find_path()
    answer1 = risk.dijkstra()
    print("PART1: %d" % answer1)

    risk.expand()
    answer2 = risk.dijkstra()
    print("PART2: %d" % answer2)


if __name__ == "__main__":
    run()
