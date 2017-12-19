from collections import defaultdict, deque

def gen(id, to, calls, done, il, locks, queues):
    "Part 2: Program generator that runs until termination or locks."
    registers = defaultdict(int)
    def value(x):
        try: return int(x)
        except ValueError: return registers[x]
    registers['p'] = id
    i = 0
    while i >= 0 and i < len(il):
        instr, *arg = il[i].split()
        if   instr == 'add': registers[arg[0]] += value(arg[1])
        elif instr == 'set': registers[arg[0]]  = value(arg[1])
        elif instr == 'mul': registers[arg[0]] *= value(arg[1])
        elif instr == 'mod': registers[arg[0]] %= value(arg[1])
        elif instr == 'jgz':
            if value(arg[0]) > 0:
                i += value(arg[1]) - 1
        elif instr == 'snd':
            queues[to].append(value(arg[0]))
            locks[to] = False
            calls[id] += 1
        elif instr == 'rcv':
            locks[id] = True
            while not queues[id]:
                yield None
            locks[id] = False
            registers[arg[0]] = queues[id].popleft()
        i += 1
    done[id] = True

def duet(il):
    "Duet of two program generators that runs until termination or deadlock."
    P = lambda id, to: gen(id, to, calls, done, il[:], locks, queues)
    calls = defaultdict(int)
    done, locks = defaultdict(bool), defaultdict(bool)
    queues = defaultdict(deque)
    p1, p2 = P(0, 1), P(1, 0)
    while (not locks[0] or not locks[1]) and (not done[0] or not done[1]):
        try:
            next(p1)
            next(p2)
        except StopIteration:
            pass
    return calls[1]

with open('./input.txt') as f:
    il = [x.strip() for x in f.readlines()]
    print('2: {}'.format(duet(il)))
