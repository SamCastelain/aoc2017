#!/usr/bin/env python3.6
import argparse
from collections import defaultdict

def calculate_spiralsum(storage, column, row):
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            result += storage[(column + i, row + j)]

    storage[(column,row)] = result
    return result

parser = argparse.ArgumentParser(
        description='Calculate the result for AoC 2017 day 3')
parser.add_argument('input', metavar='N', type=int, nargs=1)

args = parser.parse_args()
input_val = args.input[0]

val = 0
storage = defaultdict(int)
column = 0
row = 0
dx = 1
dy = 0
segment_length = 1
segment_index = 0

storage[(0,0)] = 1
while val <= input_val:
    column += dx
    row += dy
    segment_index += 1

    if segment_index == segment_length:
        segment_index = 0
        dx, dy = -dy, dx

        if dy == 0:
            segment_length += 1

    val = calculate_spiralsum(storage, column, row)
    print(f'{val}: ({column}, {row})')

print(val)
