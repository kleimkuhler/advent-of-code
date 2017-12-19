from collections import defaultdict, deque

def run(il):
    "Part 1: Run an instruction list and return the first succesful `rcv`."
    registers, frequencies = defaultdict(int), defaultdict(int)
    def value(x):
        try: return int(x)
        except ValueError: return registers[x]
    i = 0
    while i >= 0 and i < len(il):
        instr, *arg = il[i].split()
        if   instr == 'add': registers[arg[0]]  += value(arg[1])
        elif instr == 'snd': frequencies[arg[0]] = registers[arg[0]]
        elif instr == 'set': registers[arg[0]]   = value(arg[1])
        elif instr == 'mul': registers[arg[0]]  *= value(arg[1])
        elif instr == 'mod': registers[arg[0]]  %= value(arg[1])
        elif instr == 'jgz':
            if value(arg[0]) > 0:
                i += value(arg[1]) - 1
        elif instr == 'rcv':
            if frequencies[arg[0]]:
                return frequencies[arg[0]]
        i += 1

with open('./input.txt') as f:
    il = [x.strip() for x in f.readlines()]
    print('1: {}'.format(run(il)))
