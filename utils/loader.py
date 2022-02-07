#!/usr/bin/env python3
"""
Common data loader functions
"""


def load_lines(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


def load_ints_csv(filepath):
    """
    Load a from file with single line of comma seperated ints
    """
    with open(filepath) as file:
        lines = file.readlines()
        if len(lines) != 1:
            raise RuntimeError("Unexpected lines in file")

        # Convert line to list of integers
        values = lines[0].split(',')
        integers = [int(x) for x in values]
        return integers


def load_strings(filepath):
    """
    Load from file with 1 string per line
    """
    with open(filepath) as file:
        lines = file.readlines()

        # format the strings
        strings = [line.strip() for line in lines]
        return strings
