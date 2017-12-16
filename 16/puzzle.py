cat = ''.join

def dance(programs, moves, repeat=1):
    seen = []
    for i in range(repeat):
        perm = cat(programs)
        if perm in seen:
            return seen[repeat % len(seen)]
        seen.append(perm)

        for move in moves:
            if move[0] == 's':
                shift = move[1:]
                programs = programs[len(programs)-int(shift):] + programs[:len(programs)-int(shift)]
            if move[0] == 'x':
                a, b = move[1:].split('/')
                programs[int(a)], programs[int(b)] = programs[int(b)], programs[int(a)]
            if move[0] == 'p':
                ai = programs.index(move[1])
                bi = programs.index(move[3])
                programs[ai], programs[bi] = programs[bi], programs[ai]
    return programs

with open('./input.txt') as f:
    programs = [x for x in 'abcdefghijklmnop']
    moves = f.read().strip().split(',')
    print('1: {}'.format(cat(dance(programs[:], moves))))
    print('2: {}'.format(cat(dance(programs[:], moves, 1000000000))))
