def reverse(hash, x, length, inc):
    for i in range(0, (length//2)):
        lo = inc(x, i)
        hi = inc(x-i-1, length)
        hash[lo], hash[hi] = hash[hi], hash[lo]
    return hash

def compute(lengths):
    hash = [x for x in range(0, 256)]
    inc = lambda x, y: (x + y) % len(hash)
    pos, skip = 0, 0
    for length in lengths:
        reverse(hash, pos, length, inc)
        pos += inc(length, skip)
        skip += 1
    return hash

with open('./input.txt') as f:
    lengths = [int(x.strip()) for x in f.readline().split(',')]
    hash = compute(lengths)
    check = hash[0] * hash[1]
    print('a: {}'.format(check))

