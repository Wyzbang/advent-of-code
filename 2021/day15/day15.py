#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/15
"""
import copy
import sys

from utils.grid import Grid


class Risk(Grid):

    def __init__(self, data):
        super(Risk, self).__init__(data)

        # Recursive
        self.shortest_len  = None
        self.shortest_path = None

        # Dijkstra
        self.unvisited = []
        self.scores = Grid.initialize(self.width, self.height, sys.maxsize)

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
        for i, j in self.unvisited:
            if self.scores[i][j] < lowest:
                lowest = self.scores[i][j]
                node = (i, j)
        return node

    def visit(self, i, j):
        print("Visiting %d, %d..." % (i, j), end='\r')
        for n, m in self.unvisited_adjacent(i, j):
            new_score = self.scores[i][j] + self[n][m]
            if new_score < self.scores[n][m]:
                self.scores[n][m] = new_score
        self.unvisited.remove((i, j))

    def dijkstra(self):
        """
        Using Dijkstra's algorithm to find path
        :return:
        """
        for i in range(self.height):
            for j in range(self.width):
                self.unvisited.append((i, j))

        self.scores[0][0] = 0
        while len(self.unvisited):
            lowest = self.find_lowest()
            self.visit(*lowest)

        f, g = self.max()
        return self.scores[f][g]


def run():
    print("Advent of Code 2021 - Day 15")
    risk = Risk.load_digits("example.txt")
    #score, path = risk.find_path()
    score = risk.dijkstra()
    # TODO:
    print("PART1: %d" % (score))
    print("PART2: ")


if __name__ == "__main__":
    run()