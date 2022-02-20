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


class Lights(Grid):

    def __init__(self):
        self.grid = [[False for i in range(1000)] for j in range(1000)]

    def _process(self, action):
        for i in range(action.start[0], action.end[0] + 1):
            for j in range(action.start[1], action.end[1] + 1):
                if action.action == ActionType.ON:
                    value = True
                elif action.action == ActionType.OFF:
                    value = False
                elif action.action == ActionType.TOGGLE:
                    value = not self.get(i, j)

                self.set(i, j, value)

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

    print("PART1: ", lights.count(True))
    print("PART2: ")


if __name__ == "__main__":
    run()
