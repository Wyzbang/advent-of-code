#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/
"""
from enum import Enum
from utils.grid import Grid
from utils.loader import load_strings
from utils.progress import Thermometer


class ActionType(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3


class Action:

    def __init__(self, line):
        if "turn on" in line:
            self.action = ActionType.ON
            start = 8
        elif "turn off" in line:
            self.action = ActionType.OFF
            start = 9
        elif "toggle" in line:
            self.action = ActionType.TOGGLE
            start = 7

        # TODO: get range
        coords = line[start:].split(" through ")
        self.start = [int(i) for i in coords[0].split(',')]
        self.end = [int(i) for i in coords[1].split(',')]


class Lights():

    def __init__(self):
        self.a = Grid.initialize(1000, 1000, False)
        self.b = Grid.initialize(1000, 1000, 0)

    def _process(self, action):
        for i in range(action.start[0], action.end[0] + 1):
            for j in range(action.start[1], action.end[1] + 1):
                if action.action == ActionType.ON:
                    self.a.set(i, j, True)
                    value = self.b.get(i, j) + 1
                    self.b.set(i, j, value)
                elif action.action == ActionType.OFF:
                    self.a.set(i, j, False)
                    value = self.b.get(i, j) - 1
                    value = value if value >=0 else 0
                    self.b.set(i, j, value)
                elif action.action == ActionType.TOGGLE:
                    value = not self.a.get(i, j)
                    self.a.set(i, j, value)
                    value = self.b.get(i, j) + 2
                    self.b.set(i, j, value)

    def process(self):
        actions = []
        for line in load_strings("input.txt"):
            actions.append(Action(line))

        progress = Thermometer(len(actions))
        for i, action in enumerate(actions):
            self._process(action)
            progress.display(i)


def run():
    print("Advent of Code 2015 - Day 6")
    lights = Lights()
    lights.process()

    print("PART1: ", lights.a.count(True))
    print("PART2: ", lights.b.sum())


if __name__ == "__main__":
    run()
