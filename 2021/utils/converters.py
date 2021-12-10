#!/usr/bin/env python3
"""
Utilities for converting data
"""


def split(word):
    """
    Split string into list of characters
    """
    return [char for char in word]


def split_digits(word):
    """
    Split string into list of integers
    """
    return [int(char) for char in word]
