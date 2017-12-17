#!/usr/bin/env python3.6
import argparse

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 9')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

def count_garbage(char_iter):
    count = 0
    for char in char_iter:
        if char == '!':
            next(char_iter)
        elif char == '>':
            return count
        else:
            count += 1

    raise(ValueError())

def process_groups(char_iter):
    accu = 0
    for char in char_iter:
        if char == '{':
            accu += process_groups(char_iter)
        elif char == '<':
            accu += count_garbage(char_iter)
        elif char == '}':
            return accu

    return accu

with open(args.file[0]) as f:
    for line in f:
        line_iter = iter(line)
        #skip first '{'
        next(line_iter)
        value = process_groups(line_iter)
        print(value)
