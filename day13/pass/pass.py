#!/usr/bin/env python3.6
import argparse
import re

def parse_line(line):
    parse_string = '(\d+): (\d+)'

    m = re.search(parse_string, line)
    groups = m.groups()
    depth = int(groups[0])
    scan_range = int(groups[1])

    return depth, scan_range


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 13')
parser.add_argument('file', metavar='file', type=str)

args = parser.parse_args()

layers = []
with open(args.file) as f:
    for line in f:
        depth, scan_range = parse_line(line.strip())
        # A scanner returns to the top of the range with a period:
        # (range - 1) * 2.
        period = (scan_range - 1) * 2
        layers.append((depth, period))

wait_time = 0
solution_found = False
while not solution_found:
    solution_found = True
    for depth, period in layers:
        if ((wait_time + depth) % period) == 0:
            solution_found = False
            wait_time += 1
            break

print(wait_time)
