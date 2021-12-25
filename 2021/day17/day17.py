#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/17
"""
import math


class Target:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        assert x1 < x2
        assert y1 < y2

    def hit(self, x, y):
        return (x >= self.x1) and (x <= self.x2) and (y >= self.y1) and (y <= self.y2)

    def beyond(self, x, y):
        """
        Probe is beyond target, if past the right of the target or below the target
        :param x: current x position
        :param y: current y position
        :return: boolean
        """
        return x > self.x2 or y < self.y2


class Probe:

    def __init__(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.path = []

    def step(self):
        self.x += self.vx
        self.y += self.vy

        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1

        self.vy -= 1
        self.path.append((self.x, self.y))

    @property
    def location(self):
        return self.x, self.y

    def find_highest(self, target):
        self.x, self.y = 0, 0

        highest = 0
        hit = False
        while not target.beyond(*self.location):
            self.step()
            highest = self.y if self.y > highest else highest
            hit = target.hit(*self.location)

        return hit, highest


def part1math(target):
    """
    CHEAT: Found this formula in a forum to get value (used as comparison
    https://www.reddit.com/r/adventofcode/comments/ri9kdq/2021_day_17_solutions/
    """
    n = -target.y1 - 1
    answer = int(n * (n + 1) / 2)
    return answer


def part1(target):
    max = 0
    xmin = int(math.sqrt(target.x1))
    xmax = target.x2
    ymin = target.y1
    ymax = abs(target.y1) + 1

    for vx in range(xmin, xmax):
        for vy in range(ymin, ymax):
            probe = Probe(vx, vy)
            hit, highest = probe.find_highest(target)
            if hit and highest > max:
                max = highest
    return max


def run():
    print("Advent of Code 2021 - Day 17")

    # target area: x=25..67, y=-260..-200
    target = Target(25, 67, -260, -200)

    answer1m = part1math(target)
    answer1c = part1(target)
    assert answer1m == answer1c

    print("PART1: Highest =", answer1c)
    print("PART2: ")


if __name__ == "__main__":
    run()
