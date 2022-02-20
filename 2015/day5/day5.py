#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/5
"""
from utils.loader import load_strings


def isNice(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    bad = ['ab', 'cd', 'pq', 'xy']

    # if contains 3 vowels
    count = 0
    for vowel in vowels:
        count += name.count(vowel)
    hasVowels = count >= 3

    # if has double
    hasDouble = False
    for i in range(1, len(name)):
        if name[i-1] == name[i]:
            hasDouble = True
            break

    # Unless it contains bad combos
    noBad = True
    for combo in bad:
        if combo in name:
            noBad = False

    return hasVowels and hasDouble and noBad


def isNice2(name):
    """
    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    hasPair = False
    for i in range(len(name)):
        if i+2 >= len(name):
            break
        match = name[i:i+2]
        if match in name[i+2:]:
            hasPair = True
            break

    hasSplit = False
    for i, char in enumerate(name):
        if i+2 >= len(name):
            break
        if name[i+2] == char:
            hasSplit = True
            break

    return hasPair and hasSplit


def run():
    print("Advent of Code 2015 - Day 5")
    # TODO:
    names = load_strings("input.txt")

    count = 0
    for name in names:
        if isNice(name):
            count += 1

    print("PART1: ", count)

    count2 = 0
    for name in names:
        if isNice2(name):
            count2 += 1
    print("PART2: ", count2)


if __name__ == "__main__":
    run()
