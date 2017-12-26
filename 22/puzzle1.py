DIRECTIONS = UP, RIGHT, DOWN, LEFT = (0, -1), (1, 0), (0, 1), (-1, 0)

def X(point): x, y = point; return x
def Y(point): x, y = point; return y

def turn_right(dir):
    return DIRECTIONS[DIRECTIONS.index(dir) - 3]

def turn_left(dir):
    return DIRECTIONS[DIRECTIONS.index(dir) - 1]

def generator(start, infected):
    dir, infections = UP, 0
    x, y = start
    while True:
        if (x, y) in infected:
            dir = turn_right(dir)
            infected.remove((x, y))
        else:
            dir = turn_left(dir)
            infected.add((x, y))
            infections += 1
        x, y = tuple(map(sum, zip((x, y), dir)))
        yield infections

def walk(B, iterations):
    for _ in range(iterations):
        infections = next(B)
    return infections

with open('./input.txt') as f:
    lines = f.readlines()
    cur = (len(lines) // 2, len(lines[0].strip()) // 2)
    infected = {(x, y)
                for (y, row) in enumerate(lines)
                for (x, node) in enumerate(row)
                if node == '#'}
    B = generator(cur, infected)
    print('1: {}'.format(walk(B, 10000)))
