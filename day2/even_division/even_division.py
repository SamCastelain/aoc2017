#!/usr/bin/env python3.6
import argparse
import sys

def find_even_division(row):
    row.sort(reverse=True)
    for i in range(len(row) - 1):
        for divisor in row[(i + 1):]:
            if row[i] % divisor == 0:
                return row[i] // divisor

    return 0

parser = argparse.ArgumentParser(
        description='Calculate the sum of the even divisions for AoC 2017 day 2')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

result = 0
with open(args.file[0]) as f:
    for line in f:
        row = [int(number) for number in line.split()]
        result += find_even_division(row)

print(result)
