from collections import defaultdict

blueprints = {
    'A': [(1, -1, 'B'), (0, 1, 'D')],
    'B': [(1, -1, 'C'), (0, -1, 'F')],
    'C': [(1, 1, 'C'), (1, 1, 'A')],
    'D': [(0, 1, 'E'), (1, -1, 'A')],
    'E': [(1, 1, 'A'), (0, -1, 'B')],
    'F': [(0, -1, 'C'), (0, -1, 'E')],
}

def run(state, iterations=1):
    tape = defaultdict(int)
    cur = 0
    for _ in range(iterations):
        tape[cur], move, state = blueprints[state][tape[cur]]
        cur += move
    return tape

print('1: {}'.format(sum(run('A', 12317297).values())))
