#!/usr/bin/env python3.6
import argparse
import sys

parser = argparse.ArgumentParser(
        description='Calculate the checksum for AoC 2017 day 2')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

checksum = 0
with open(args.file[0]) as f:
    for line in f:
        min_cell = sys.maxsize
        max_cell = 0
        for number in line.split():
            number = int(number)
            if number < min_cell:
                min_cell = number
            if number > max_cell:
                max_cell = number
        checksum += max_cell - min_cell

print(checksum)
