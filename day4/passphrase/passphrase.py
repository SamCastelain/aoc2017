#!/usr/bin/env python3.6
import argparse
import sys

parser = argparse.ArgumentParser(
        description='Count the valid passphrases for AoC 2017 day 4')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

valid_phrases = 0
with open(args.file[0]) as f:
    for line in f:
        words = line.split()
        words_set = {word for word in words}
        if len(words_set) == len(words):
            valid_phrases += 1

print(valid_phrases)
