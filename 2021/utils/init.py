#!/usr/bin/env python3
"""
Utilities for converting data
"""


def gen_array(width, value):
    """
    Generate an list of size 'width' with each set to 'value'
    """
    return [value for i in range(width)]


def gen_grid(width, height, value):
    """
    Generate a grid (list of lists) of size WxH with each cell set to 'value'
    """
    return [[value for i in range(width)] for j in range(height)]
