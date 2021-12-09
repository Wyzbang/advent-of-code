#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/8
"""


def split(word):
    return [char for char in word]


def has_all(l1, l2):
    """

    :param l1: string to check
    :param l2: values to check againsts
    :return:
    """
    for c in l2:
        if c not in l1:
            return False
    return True


def alpha(s):
    return "".join(sorted(split(s)))


class Signal:

    def __init__(self, data):
        tmp = data.split('|')
        self.inputs = tmp[0].split()
        self.outputs = tmp[1].split()
        self.numbers = ["" for i in range(10)]

        for i, value in enumerate(self.inputs):
            self.inputs[i] = alpha(value)
        for i, value in enumerate(self.outputs):
            self.outputs[i] = alpha(value)

    def decoder(self, value):
        if value in self.numbers:
            # break early if value has already been decoded
            return True

        if len(value) == 2:
            # can only be '1' so these two values can only be in segment 2 or 5
            self.numbers[1] = value

        elif len(value) == 3:
            # can only be '7' so these two values can only be in segment 0, 2 or 5
            self.numbers[7] = value

        elif len(value) == 4:
            # can only be '4' so these two values can only be in segment 1, 2, 3 or 5
            self.numbers[4] = value

        elif len(value) == 7:
            # can only be 8
            self.numbers[8] = value

        elif len(value) == 5:
            # 2,3,5 -> 5 segments
            # if value has all  in 7 => 3
            # elif 6 has all in value => 5
            # else -> 2
            if self.numbers[7] == "":
                return False
            elif has_all(value, self.numbers[7]):
                self.numbers[3] = value
            elif self.numbers[6] == "":
                return False
            elif has_all(self.numbers[6], value):
                self.numbers[5] = value
            else:
                self.numbers[2] = value

        elif len(value) == 6:
            # 0,6,9 -> 6 segments
            # if value has all  in 4 => 9
            # elif value has all in 7 => 0
            # else -> 6
            if self.numbers[4] == "":
                return False
            elif has_all(value, self.numbers[4]):
                self.numbers[9] = value
            elif self.numbers[7] == "":
                return False
            elif has_all(value, self.numbers[7]):
                self.numbers[0] = value
            else:
                self.numbers[6] = value

        return True

    def decode(self):
        undecoded = []
        for value in self.inputs + self.outputs:
            if not self.decoder(value):
                undecoded.append(value)

        # second pass at decoding once 1, 4, 7, 8 have been determined
        for value in undecoded:
            self.decoder(value)

        undecoded = []
        for value in undecoded:
            if not self.decoder(value):
                undecoded.append(value)

        for value in self.outputs:
            if value not in self.numbers:
                raise RuntimeError('undecoded value found')

    def output(self):
        digits = []
        for value in self.outputs:
            digits.append(self.numbers.index(value))

        strings = [str(integer) for integer in digits]
        number = int("".join(strings))
        return number


def load():
    with open("input.txt") as file:
        lines = file.readlines()
        signals = []

        # Format read data
        for line in lines:
            signals.append(Signal(line))

        return signals


def run(signals):
    answer = 0
    for signal in signals:
        for output in signal.outputs:
            if len(output) in [2, 4, 3, 7]:
                answer += 1
    print("PART1: ", answer)

    total = 0
    for signal in signals:
        signal.decode()
        total += signal.output()
    print("PART1: ", total)

def test():
    a = Signal("abd ad | sd add")
    a.remove(0, 'a')
    print(a.decoded)
    b = Signal("abd ad | sd add")
    b.remove_not(0, 'a')
    print(b.decoded)


if __name__ == "__main__":
    # test()
    print("Advent of Code 2021 - Day 8")
    parsed = load()
    run(parsed)
