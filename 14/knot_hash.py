import operator

from functools import reduce

def compute(lengths, repeat=1):
    hash = [x for x in range(256)]
    inc = lambda x, y: (x + y) % len(hash)
    pos, skip = 0, 0
    for _ in range(repeat):
        for length in lengths:
            indices = [inc(pos, x) for x in range(length)]
            values = reversed([hash[x] for x in indices])
            for i, v in zip(indices, values):
                hash[i] = v
            pos += inc(length, skip)
            skip += 1
    return hash

def dense(sparse):
    out = ''
    for i in range(0, len(sparse), 16):
        block = [sparse[j] for j in range(i, i+16)]
        n = reduce(operator.xor, block)
        h = hex(n)
        out += '0' + h[2:] if len(h) == 3 else h[2:]
    return out
