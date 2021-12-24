#!/usr/bin/env python3
"""
https://adventofcode.com/2021/day/16
"""
import sys

from bitarray import bitarray
from bitarray.util import hex2ba, ba2int
from enum import Enum
from utils.loader import load_lines


def load_bits(filepath):
    lines = load_lines(filepath)
    assert len(lines) == 1

    str = lines[0].strip()
    for char in str:
        assert char in "0123456789ABCDEF"

    bits = hex2ba(str)

    return bits


class PacketType(Enum):
    OPA = 3
    LITERAL = 4
    OPB = 6


class Packet:

    def __init__(self, version, ptype):
        self.__version = version
        self.__ptype = ptype

        # Literal Attributes
        self.__value = None

        # Operator Attributes
        self.lengthID = None
        self.length = None
        self.packets = []

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version):
        if type(version) is bitarray:
            converted = ba2int(version)
            self.__version = converted
        else:
            self.__version = version

    @property
    def ptype(self):
        return self.__ptype

    @ptype.setter
    def ptype(self, ptype):
        if type(ptype) is bitarray:
            converted = ba2int(ptype)
            self.__ptype = converted
        else:
            self.__ptype = ptype

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) is bitarray:
            converted = ba2int(value)
            self.__value = converted
        else:
            self.__value = value

    @classmethod
    def literal(cls, version, ptype, value):
        new = cls(version, ptype)
        new.value = value
        return new

    @classmethod
    def operator(cls, version, ptype, packets, lengthID, length):
        new = cls(version, ptype)
        new.packets = packets
        new.lengthID = lengthID
        new.length = length
        return new

    def dump(self, prefix=""):
        if self.ptype == PacketType.LITERAL.value:
            print("%sL %d %d = %d" % (prefix, self.version, self.ptype, self.value))
        else:
            print("%sO %d %d %d%s" % (prefix, self.version, self.ptype, self.length, self.lengthID))
        for packet in self.packets:
            packet.dump(prefix + "-")


def pad(index, sub_packet):
    """
    Only pad to next HEX if this is a root packet
    :param index:
    :param sub_packet:
    :return:
    """
    padding = 0
    if not sub_packet:
        rem = index % 8
        padding = 8 - rem if rem > 0 else 0
    return padding


def parse(bits, sub_packet=False, count=sys.maxsize):
    header = True
    index = 0

    packets = []
    data = bitarray()

    while index < len(bits) and len(packets) < count:
        if header:
            data = bitarray()

            version = ba2int(bits[index:index+3])
            index += 3
            ptype = ba2int(bits[index:index+3])
            index += 3
            header = False

        elif ptype == 4:
            last = bits[index] == 0
            data.extend(bits[index+1:index+5])
            index += 5
            if last:
                new = Packet.literal(version, ptype, data)
                packets.append(new)

                # Reset for next Packet
                padding = pad(index, sub_packet)
                index += padding
                header = True

        else:
            # 0 = next 15 bits > size in bytes for sub-packets
            # 1 = next 11 buts > number of sub-packets
            lengthID = ba2int(bits[index:index+1])
            index += 1
            if lengthID == 0:
                length = ba2int(bits[index:index+15])
                index += 15
                end = index + length
                inc, sub = parse(bits[index:end], True)
                new = Packet.operator(version, ptype, sub, "bits", length)
                packets.append(new)
                index += length

                # Reset for next Packet
                padding = pad(index, sub_packet)
                index += padding
                header = True

            if lengthID == 1:
                sub_count = ba2int(bits[index:index+11])
                index += 11
                inc, sub = parse(bits[index:], True, sub_count)
                new = Packet.operator(version, ptype, sub, "packets", sub_count)
                packets.append(new)
                index += inc

                # Reset for next Packet
                padding = pad(index, sub_packet)
                index += padding
                header = True

    return index, packets


def sum_version(packets):
    total = 0
    for packet in packets:
        total += sum_version(packet.packets)
        total += packet.version
    return total


def run():
    print("Advent of Code 2021 - Day 16")
    bits = load_bits("input.txt")
    i, packets = parse(bits)

    for packet in packets:
        packet.dump()

    answer1 = sum_version(packets)

    # TODO: Part 2
    answer2 = 0

    print("PART1: ", answer1)
    print("PART2: ", answer2)


if __name__ == "__main__":
    run()
