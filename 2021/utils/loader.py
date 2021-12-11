#!/usr/bin/env python3
"""
Common data loader functions
"""


def load_strings(filepath):
    with open(filepath) as file:
        lines = file.readlines()

    data = [line.strip() for line in lines]
    return data
