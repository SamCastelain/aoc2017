#!/usr/bin/env python3.6
import argparse

class CubeHex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return (abs(other.x - self.x) + abs(other.y - self.y)
                + abs(other.z - self.z)) // 2

    def __add__(self, other):
        return CubeHex(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return '"({}, {}, {})"'.format(self.x, self.y, self.z)


DIRECTIONS = {
    'n': CubeHex(0, 1, -1),
    'ne': CubeHex(1, 0, -1),
    'se': CubeHex(1, -1, 0),
    's': CubeHex(0, -1, 1),
    'sw': CubeHex(-1, 0, 1),
    'nw': CubeHex(-1, 1, 0),
}


def calc_furthest_distance(line):
    orig_cube = CubeHex(0, 0, 0)

    cube = orig_cube
    furthest = 0
    for direction in line.split(','):
        cube = cube + DIRECTIONS[direction]
        distance = orig_cube.distance(cube)
        furthest = max(furthest, distance)

    return furthest

parser = argparse.ArgumentParser(
        description='Solution for part 2 of day 11')
parser.add_argument('file', metavar='file', type=str)

args = parser.parse_args()

with open(args.file) as f:
    for line in f:
        value = calc_furthest_distance(line.strip())
        print(value)
