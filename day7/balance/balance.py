#!/usr/bin/env python3.6
import argparse
import re
from collections import defaultdict

#Messy solution, but good enough for now

def all_equal(values):
    iterator = iter(values)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


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

    def check_balanced(self, tower):
        weights = []
        for child in self.children:
            child_weight = tower[child].check_balanced(tower)
            weights.append(child_weight)

        if not all_equal(weights):
            print(', '.join([str(tower[child].weight) for child in self.children]))
            print(weights)

        return self.weight + sum(weights)

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

tower[no_parents.pop()].check_balanced(tower)
