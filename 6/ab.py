from itertools import count
from itertools import cycle
from itertools import islice

def a(A):
    configs = set()
    for steps in count(1):
        bank = A.index(max(A))
        dist, A[bank] = A[bank], 0
        banks = cycle(range(len(A)))
        banks_start = islice(banks, bank+1, None)

        while dist != 0:
            A[next(banks_start)] += 1
            dist -= 1

        if tuple(A) not in configs:
            configs.add(tuple(A))
        else:
            return steps

def b(A):
    configs = dict()
    for steps in count(1):
        bank = A.index(max(A))
        dist, A[bank] = A[bank], 0
        banks = cycle(range(len(A)))
        banks_start = islice(banks, bank+1, None)

        while dist != 0:
            A[next(banks_start)] += 1
            dist -= 1

        if tuple(A) not in configs:
            configs[tuple(A)] = steps
        else:
            return steps - configs[tuple(A)]

with open("./input.txt") as f:
    memory_banks = [int(x.strip()) for x in f.readline().split()]
    print("a: {}".format(a(memory_banks[:])))
    print("b: {}".format(b(memory_banks[:])))
