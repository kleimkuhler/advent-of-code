import re

from collections import defaultdict
from itertools import product

lcat = '/'.join
ccat = ''.join
split = lambda patt: patt.split('/')
square_size = lambda length: 2 if length % 2 == 0 else 3

def reflect(patt):
    return lcat([line[::-1] for line in split(patt)])

def flip(patt):
    return lcat([line for line in split(patt)[::-1]])

def rotate(patt):
    return lcat([ccat(line) for line in zip(*split(patt))])

def expand(rules):
    "Expand transforms to include all transformation patterns."
    for k, v in rules.items():
        v.append(reflect(v[-1]))
        v.append(flip(v[-1]))
        v.append(reflect(v[-1]))
        v.append(rotate(v[-1]))
        v.append(reflect(v[-1]))
        v.append(flip(v[-1]))
        v.append(reflect(v[-1]))
    return rules

def transform(art, rules):
    "Transform art into enhanced art by looking through rules."
    for k, v in rules.items():
        if art in v:
            return split(k)

def enhance(art, rules, iterations=2):
    """Enhance art by deconstructing into subarts, transforming into enhanced
    art, and then constructing back into new art"""
    for _ in range(iterations):
        transformed, enhanced = [], []
        lines = split(art)
        side = square_size(len(lines[0]))
        squares = len(lines[0]) // side
        for row, col in product(*[range(0, len(lines[0]), side)]*2):
            square = lcat([line[col:col+side] for line in lines[row:row+side]])
            transformed.append(transform(square, rules))
        for col, row in product(*[range(0, len(transformed), squares)],
                                *[range(0, len(transformed[0]))]):
            square = ccat([line[row] for line in transformed[col:col+squares]])
            enhanced.append(square)
        art = lcat(enhanced)
    return art

with open('./input.txt') as f:
    begin = '.#./..#/###'
    rules = defaultdict(list)
    for line in f:
        patt, trans = line.split('=>')
        rules[trans.strip()] = [patt.strip()]
    rules = expand(rules)
    print('1: {}'.format(enhance(begin, rules, 5).count('#')))
    print('2: {}'.format(enhance(begin, rules, 18).count('#')))
