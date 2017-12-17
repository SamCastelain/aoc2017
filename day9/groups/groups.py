#!/usr/bin/env python3.6
import argparse

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 9')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

def skip_garbage(char_iter):
    for char in char_iter:
        if char == '!':
            next(char_iter)
        elif char == '>':
            return

    raise(ValueError())

def calculate_value(outer_value, char_iter):
    accu = outer_value + 1
    for char in char_iter:
        if char == '{':
            accu += calculate_value(outer_value + 1, char_iter)
        elif char == '<':
            skip_garbage(char_iter)
        elif char == '}':
            return accu

    return accu

with open(args.file[0]) as f:
    for line in f:
        line_iter = iter(line)
        #skip first '{'
        next(line_iter)
        value = calculate_value(0, line_iter)
        print(value)
