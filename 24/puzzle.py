import re

from collections import defaultdict

def components(pairs):
    comps = defaultdict(set)
    for pair in pairs:
        comps[pair[0]].add(pair)
        comps[pair[1]].add(pair)
    return comps

def bridges(comps, bridge=(), port=0):
    if bridge: yield bridge
    for comp in comps[port]:
        if comp not in bridge:
            yield from bridges(comps,
                               bridge+(comp,),
                               comp[0] if port == comp[1] else comp[1])

with open('./input.txt') as f:
    pairs = [tuple(map(int, line.split('/'))) for line in f]
    comps = components(pairs)
    valid = []
    for bridge in bridges(comps):
        valid.append((bridge, sum(a+b for a, b in bridge), len(bridge)))
    print('1: {}'.format(sorted(valid, key=lambda v: v[1])[-1][1]))
    print('2: {}'.format(sorted(valid, key=lambda v: v[2])[-1][1]))
