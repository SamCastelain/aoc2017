#!/usr/bin/env python3.6
import argparse
import re

class Program:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def __repr__(self):
        if self.children:
            return '"{} ({}) -> {}"'.format(
                    self.name, self.weight, ', '.join(self.children))
        else:
            return '"{} ({})"'.format(self.name, self.weight)

def parse_line(line):
    parse_string = '(\w+) \((\d+)\)(?: -> (.*))?'

    m = re.search(parse_string, line)
    groups = m.groups()
    name  = groups[0]
    weight = int(groups[1])
    children = []
    if groups[2]:
        children = [child.strip() for child in groups[2].split(',')]

    return Program(name, weight, children)

parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 6')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

tower = dict()
no_parents = set()
with open(args.file[0]) as f:
    for line in f:
        program = parse_line(line)
        tower[program.name] = program
        no_parents.add(program.name)

for key, value in tower.items():
    for child in value.children:
        no_parents.remove(child)

print(no_parents)
