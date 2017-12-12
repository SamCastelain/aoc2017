#!/usr/bin/env python3.6
import argparse
import re
from collections import defaultdict
import operator

COMPARISONS = {
    '>': operator.gt,
    '<': operator.lt,
    '<=': operator.le,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne
}

def check_condition(registers, condition_list):
    operand1 = registers[condition_list[0]]
    operand2 = int(condition_list[2])
    condition = condition_list[1]

    return COMPARISONS[condition](operand1, operand2)


def execute_line(registers, line):
    elements = line.split()

    if check_condition(registers, elements[4:]):
        operand = int(elements[2])
        if elements[1] == 'dec':
            operand = -operand

        registers[elements[0]] += operand

parser = argparse.ArgumentParser(
        description='Solution for part 2 of day 8')
parser.add_argument('file', metavar='file', type=str, nargs=1)

args = parser.parse_args()

registers = defaultdict(int)
abs_max = 0
with open(args.file[0]) as f:
    for line in f:
        execute_line(registers, line)
        max_value = max(registers.items(), key=operator.itemgetter(1))[1]
        if max_value > abs_max:
            abs_max = max_value

print(abs_max)
