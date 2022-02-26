#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/7
"""
from utils.loader import load_strings


class Wiring:

    def __init__(self, actions):
        self.wires = {}
        todo = actions

        while todo:
            print("Processing ", len(todo), end='\r')
            skipped = []
            for action in actions:
                try:
                    self.wire(action)
                except KeyError:
                    # one of the wires has not been set yet
                    skipped.append(action)

            todo = skipped

    def wire(self, action):
        temp = action.split(" -> ")
        target = temp[1]
        operation = temp[0]

        if "AND" in operation:
            a, b = operation.split(" AND ")
            value = self[a] & self[b]

        elif "OR" in operation:
            a, b = operation.split(" OR ")
            value = self[a] | self[b]

        elif "LSHIFT" in operation:
            a, b = operation.split(" LSHIFT ")
            value = self[a] << int(b)

        elif "RSHIFT" in operation:
            a, b = operation.split(" RSHIFT ")
            value = self[a] >> int(b)

        elif "NOT" in operation:
            a = operation[4:]
            value = self[a] ^ 65535

        else:
            value = self[operation]

        self.wires[target] = value

    def __getitem__(self, item):
        try:
            value = int(item)
        except ValueError:
            value = self.wires[item]

        return value


def run():
    print("Advent of Code 2021 - Day ")
    # TODO:
    actions = load_strings("input.txt")
    wiring = Wiring(actions)

    print("PART1: ", wiring['a'])

    actions = load_strings("inputb.txt")
    wiring = Wiring(actions)
    print("PART2: ", wiring['a'])


if __name__ == "__main__":
    run()
