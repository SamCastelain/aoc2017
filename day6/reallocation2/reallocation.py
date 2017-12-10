#!/usr/bin/env python3.6
import argparse

def rebalance(banks):
    highest_blocks = -1
    highest_index = 0
    for index, blocks in enumerate(banks):
        if blocks > highest_blocks:
            highest_blocks = blocks
            highest_index = index

    banks[highest_index] = 0
    while highest_blocks:
        highest_index = (highest_index + 1) % len(banks)
        highest_blocks -= 1
        banks[highest_index] += 1


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 6')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

banks = None
with open(args.file[0]) as f:
    for line in f:
        banks = [int(num) for num in line.split()]

steps = 0
seen = dict()
while True:
    steps += 1
    rebalance(banks)
    banks_tuple = tuple(banks)
    if banks_tuple in seen:
        print(steps - seen[banks_tuple])
        break
    else:
        seen[banks_tuple] = steps
