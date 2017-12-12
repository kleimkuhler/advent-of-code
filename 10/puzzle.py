def compute(lengths):
    hash = [x for x in range(0, 256)]
    inc = lambda x, y: (x + y) % len(hash)
    pos, skip = 0, 0
    for length in lengths:
        indices = [inc(pos, x) for x in range(length)]
        values = reversed([hash[x] for x in indices])
        for i, v in zip(indices, values):
            hash[i] = v
        pos += inc(length, skip)
        skip += 1
    return hash

with open('./input.txt') as f:
    lengths = [int(x.strip()) for x in f.readline().split(',')]
    hash = compute(lengths)
    check = hash[0] * hash[1]
    print('a: {}'.format(check))

