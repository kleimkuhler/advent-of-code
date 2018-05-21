from collections import defaultdict
from itertools import islice

def X(point): x, y = point; return x
def Y(point): x, y = point; return y

def spiral():
    x, y, length = 0, 0, 1
    yield (x, y)
    while True:
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            for _ in range(length):
                x += dx; y += dy
                yield (x, y)
            if dy: length += 1

def walk(S, N):
    return next(islice(S, N-1, None))

def mahatten_distance(point):
    return abs(X(point)) + abs(Y(point))

def neighbors8(point):
    x, y = point
    return ((x-1, y+1), (x, y+1), (x+1, y+1),
            (x-1, y),             (x+1, y),
            (x-1, y-1), (x, y-1), (x+1, y-1))

def walk_sum(S):
    grid = defaultdict(int)
    grid[next(S)] = 1
    for square in S:
        grid[square] = sum([grid[s] for s in neighbors8(square)])
        yield grid[square]

input = 325489
print('1: {}'.format(mahatten_distance(walk(spiral(), input))))
print('2: {}'.format(next(s for s in walk_sum(spiral()) if s > input)))
