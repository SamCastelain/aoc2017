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

severity = 0
with open(args.file) as f:
    for line in f:
        depth, scan_range = parse_line(line.strip())
        # A scanner returns to the top of the range with a period:
        # (range - 1) * 2. Because we move one deeper per picosecond
        # the we reach a certain depth at depth picoseconds.
        period = (scan_range - 1) * 2
        if (depth % period) == 0:
            severity += depth * scan_range

    print(severity)
