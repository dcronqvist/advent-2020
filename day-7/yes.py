import collections
import math
import re
import sys

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

lines = [l.rstrip('\n') for l in read_input_lines()]

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        ct = int(ct)
        containedin[innercolor].add(color)
        contains[color].append((ct, innercolor))

holdsgold = set()
def check(color):
    for c in containedin[color]:
        holdsgold.add(c)
        check(c)
check('shiny gold')
print(len(holdsgold))

def cost(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * cost(inner)
    return total
print(cost('shiny gold'))