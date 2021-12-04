#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/3
"""


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        codes = []
        width = len(lines[0].strip())
        for line in lines:
            code = []
            if width != len(line.strip()):
                raise RuntimeError("Mismatch bit width")
            width = len(line.strip())
            for byte in line.strip():
                code.append(int(byte))

            codes.append(code)

        print("Loaded %s codes" % (len(codes)))
        return width, codes


def count_ones(width, codes):
    ones = [0] * width
    for code in codes:
        for i, bit in enumerate(code):
            ones[i] = (ones[i] + 1) if bit == 1 else ones[i]
    return ones


def day3_part1(width, codes):
    ones = count_ones(width, codes)

    half = len(codes) / 2
    gamma = ""
    epsilon = ""
    for j, count in enumerate(ones):
        if count > half:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    answer = int(gamma, 2) * int(epsilon, 2)
    # Answer
    print("PART1: gamma=%s, epsilon=%s => %d" % (gamma, epsilon, answer))


def recurse(width, codes, position, most):
    """
    Filter down list based on value at position, if most or least used of
    the binary values (0 or 1) at that position
    """
    half = len(codes) / 2
    ones = count_ones(width, codes)
    # keep = 0

    if position > len(codes[0]):
        print("ERROR", codes)

    # Decide to keep the ones or zeros in current position
    if ones[position] >= half:
        keep = 1 if most else 0
    else:
        keep = 0 if most else 1

    # Filter the list
    sub_codes = []
    for code in codes:
        if code[position] == keep:
            sub_codes.append(code)

    if len(sub_codes) == 1:
        return sub_codes

    return recurse(width, sub_codes, position+1, most)


def bits_to_int(array):
    """
    Convert array of bits to an integer
    """
    i = 0
    for bit in array:
        i = (i << 1) | bit
    return i


def day3_part2(width, codes):
    ox_bits = recurse(width, codes, 0, True)[0]
    ox = bits_to_int(ox_bits)
    co_bits = recurse(width, codes, 0, False)[0]
    co = bits_to_int(co_bits)

    # Answer
    answer = ox * co
    print("PART2: ox %s %d,  co %s %d => %d" % (bin(ox), ox, bin(co), co, answer))


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 3")
    parsed = load()
    day3_part1(*parsed)
    day3_part2(*parsed)
