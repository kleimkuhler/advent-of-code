import re

from collections import defaultdict

def group(A, n):
    "Make m groups of size n."
    return tuple(map(tuple, [A[x:x+n] for x in range(0, len(A), n)]))

def magnitude(vec):
    "Return the magnitude of a 3 dimensional vector."
    x, y, z = vec
    return abs(x) + abs(y) + abs(z)

def minimum_reduce(D, comp, constraint):
    """Reduce the {key: value} pairs of a dict down to the minimum `comp()`
    values constrained by the keys in `constraint`"""
    return [k for k, v in D.items()
            if k in constraint
            and comp(v) == min(map(comp, [D[x] for x in constraint]))]

def closest(pos, vel, accel):
    """Find the particle closest to (0, 0, 0) after an infinte amount of ticks
    by reducing to the minimum set of accelerations, velocities, and positions
    respectively"""
    minaccel = minimum_reduce(accel, magnitude, set(accel))
    minvel = minimum_reduce(vel, magnitude, minaccel)
    minpos = minimum_reduce(pos, magnitude, minvel)
    return minpos[0]

def ticker(pos, vel, accel):
    "Tick generator that removes any particles in the same position."
    while True:
        for p in set(pos):
            vel[p] = tuple(map(sum, zip(vel[p], accel[p])))
            pos[p] = tuple(map(sum, zip(pos[p], vel[p])))
        duplicates = defaultdict(list)
        for k, v in pos.items():
            duplicates[v].append(k)
        for v in duplicates.values():
            if len(v) > 1:
                for p in v:
                    pos.pop(p)
                    vel.pop(p)
                    accel.pop(p)
        yield (pos, vel, accel)

def collide(pos, vel, accel):
    "Tick particle states until system is in an uncatchable state."
    T = ticker(pos, vel, accel)
    for _ in range(1000):
        next(T)
    return len(set(pos))

with open('./input.txt') as f:
    pos, vel, accel = defaultdict(list), defaultdict(list), defaultdict(list)
    for i, line in enumerate(f):
        p, v, a = group(tuple(map(int, re.findall(r'-?\d+', line))), 3)
        pos[i], vel[i], accel[i] = p, v, a
    print('1: {}'.format(closest(pos, vel, accel)))
    print('2: {}'.format(collide(pos, vel, accel)))
