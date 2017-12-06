#!/usr/bin/env python3.6
import argparse

parser = argparse.ArgumentParser(
        description='Calculate the Manhattan distance for AoC 2017 day 3')
parser.add_argument('input', metavar='N', type=int, nargs=1)

args = parser.parse_args()

column = 0
row = 0
dx = 1
dy = 0
segment_length = 1
segment_index = 0
for i in range(2, args.input[0] + 1):
    column += dx
    row += dy
    segment_index += 1

    if segment_index == segment_length:
        segment_index = 0
        dx, dy = -dy, dx

        if dy == 0:
            segment_length += 1

    print(f'{i}: ({column}, {row})')

print(abs(row) + abs(column))
