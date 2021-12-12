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

    def get_sub(self, path, max):
        for cave in self.connections[path[-1]]:
            new_path = copy.copy(path)
            new_path.append(cave)
            if cave == 'end':
                if new_path not in self.paths:
                    self.paths.append(new_path)
                    print("Found %d..." % (len(self.paths)), end="\r")
            elif cave in ['start', 'end']:
                pass
            elif cave.islower() and path.count(cave) > max:
                pass
            else:
                if cave.islower() and new_path.count(cave) == 2:
                    self.get_sub(new_path, 0)
                else:
                    self.get_sub(new_path, max)

    def get_paths(self, max):
        self.paths = []
        self.get_sub(["start"], max)
        return self.paths


def run():
    print("Advent of Code 2021 - Day 12")
    caves = Caves('input.txt')
    paths1 = caves.get_paths(0)
    print("PART1: Single small cave, paths: ", len(paths1))
    paths2 = caves.get_paths(1)
    print("PART2: Double first small cave, paths: ", len(paths2))


if __name__ == "__main__":
    run()
