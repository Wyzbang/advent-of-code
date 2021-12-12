#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/12
"""
import copy


class Caves:

    def __init__(self, filepath):
        self.connections = {}  # cave : [connections]
        self.load(filepath)
        self.paths = []
        self.revisits = 0

    def add_connection(self, a, b):
        if a in self.connections:
            if b not in self.connections[a]:
                self.connections[a].append(b)
        else:
            self.connections[a] = [b]

    def load(self, filepath):
        with open(filepath) as file:
            lines = file.readlines()

        for line in lines:
            a, b = line.strip().split('-')
            self.add_connection(a, b)
            if b != 'end':
                self.add_connection(b, a)

    def get_sub(self, path):
        for cave in self.connections[path[-1]]:
            new_path = copy.copy(path)
            new_path.append(cave)
            if cave == 'end':
                self.paths.append(new_path)
            elif cave.islower() and cave in path:
                pass
            else:
                self.get_sub(new_path)

    def get_paths(self):
        self.paths = []
        self.get_sub(["start"])
        return self.paths


def run():
    print("Advent of Code 2021 - Day 12")
    caves = Caves('input.txt')
    paths1 = caves.get_paths()
    paths2 = []
    print("PART1: ", len(paths1))
    print("PART2: ", len(paths2))


if __name__ == "__main__":
    run()
