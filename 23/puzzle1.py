from collections import defaultdict, deque

def run(il):
    "Part 1: Run an instruction list and return the first succesful `rcv`."
    registers = defaultdict(int)
    def value(x):
        try: return int(x)
        except ValueError: return registers[x]
    i, mul = 0, 0
    while i >= 0 and i < len(il):
        instr, *arg = il[i].split()
        if   instr == 'set': registers[arg[0]]  = value(arg[1])
        elif instr == 'sub': registers[arg[0]] -= value(arg[1])
        elif instr == 'mul':
            registers[arg[0]] *= value(arg[1])
            mul += 1
        elif instr == 'jnz':
            if value(arg[0]) != 0:
                i += value(arg[1]) - 1
        i += 1
    return mul

with open('./input.txt') as f:
    il = [x.strip() for x in f.readlines()]
    print('1: {}'.format(run(il)))
