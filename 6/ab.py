from itertools import count
from itertools import cycle
from itertools import islice

def ab(A):
    configs = dict()
    for steps in count(1):
        bank = A.index(max(A))
        dist, A[bank] = A[bank], 0
        banks = islice(cycle(range(len(A))), bank+1, None)

        while dist != 0:
            A[next(banks)] += 1
            dist -= 1

        if tuple(A) not in configs:
            configs[tuple(A)] = steps
        else:
            return (steps, steps - configs[tuple(A)])

with open("./input.txt") as f:
    memory_banks = [int(x.strip()) for x in f.readline().split()]
    a, b = [x for x in ab(memory_banks[:])]
    print("a: {}".format(a))
    print("b: {}".format(b))
