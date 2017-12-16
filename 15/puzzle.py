last_int = lambda line: int([x for x in line.strip().split()].pop())
agen = lambda seed: generator(seed, 16807)
bgen = lambda seed: generator(seed, 48271)

def generator(prev, factor, mod=2147483647):
    while True:
        prev = (prev * factor) % mod
        yield prev

def duel(agen, bgen, repeat=5, bits=16):
    match = 2**bits
    return sum(next(agen) % match == next(bgen) % match
               for _ in range(repeat))

with open('./input.txt') as f:
    aseed = last_int(f.readline())
    bseed = last_int(f.readline())
    r1, r2 = 40000000, 5000000

    print('1: {}'.format(duel(agen(aseed), bgen(bseed), r1)))
    print('2: {}'.format(duel(filter(lambda x: x % 4 == 0, agen(aseed)),
                              filter(lambda x: x % 8 == 0, bgen(bseed)),
                              r2)))

