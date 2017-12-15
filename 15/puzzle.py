r1, r2, afac, bfac = 40000000, 5000000, 16807, 48271

agen = lambda seed: generator(seed, afac)
bgen = lambda seed: generator(seed, bfac)
last_int = lambda line: int([x for x in line.strip().split()].pop())

def generator(prev, factor, mod=2147483647):
    while True:
        prev = (prev * factor) % mod
        yield prev

def duel(agen, bgen, repeat=5, bits=16):
    match = 2**bits
    count = 0
    for _ in range(repeat):
        if next(agen) % match == next(bgen) % match:
            count += 1
    return count

with open('./input.txt') as f:
    aseed = last_int(f.readline())
    bseed = last_int(f.readline())

    print('1: {}'.format(duel(agen(aseed), bgen(bseed), r1)))
    print('2: {}'.format(duel(filter(lambda x: x % 4 == 0, agen(aseed)),
                              filter(lambda x: x % 8 == 0, bgen(bseed)),
                              r2)))

