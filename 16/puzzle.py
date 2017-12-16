def dance(programs, moves):
    "Generate an infinite sequence of program permutations according to moves."
    while True:
        for move in moves:
            if move[0] == 's':
                shift = move[1:]
                programs = programs[len(programs)-int(shift):] + programs[:len(programs)-int(shift)]
            elif move[0] == 'x':
                a, b = move[1:].split('/')
                programs[int(a)], programs[int(b)] = programs[int(b)], programs[int(a)]
            elif move[0] == 'p':
                ai = programs.index(move[1])
                bi = programs.index(move[3])
                programs[ai], programs[bi] = programs[bi], programs[ai]
        yield ''.join(programs)

def routine(D, repeat):
    "Which program permutation will the `repeat` repetition be?"
    seen = []
    for _ in range(repeat):
        perm = next(D)
        if perm in seen:
            return seen[repeat % len(seen) - 1]
        seen.append(perm)

with open('./input.txt') as f:
    programs = [x for x in 'abcdefghijklmnop']
    moves = f.read().strip().split(',')
    D = lambda programs, moves: dance(programs, moves)

    print('1: {}'.format(next(D(programs[:], moves))))
    print('2: {}'.format(routine(D(programs[:], moves), 10**9)))
