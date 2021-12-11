#!/usr/bin/env python3
"""
Common data loader functions
"""
from utils.converters import split_digits


def load_strings(filepath):
    with open(filepath) as file:
        lines = file.readlines()

    data = [line.strip() for line in lines]
    return data


def load_grid_digits(filepath):
    """
    Load a grid (2d list) of integer digits
    :param filepath:
    :return:
    """
    with open(filepath) as file:
        lines = file.readlines()
        data = []
        # Format read data
        for line in lines:
            data.append(split_digits(line.strip()))
        return data
