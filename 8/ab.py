import operator

ops = {
    'inc' : operator.add,
    'dec' : operator.sub,
    '>'   : operator.gt,
    '<'   : operator.lt,
    '>='  : operator.ge,
    '<='  : operator.le,
    '=='  : operator.eq,
    '!='  : operator.ne,
}


def ab(instructions):
    regs = {}
    max_val = 0
    for instr in instructions:
        # Add register if new
        if instr[0] not in regs:
            regs[instr[0]] = 0
        if instr[4] not in regs:
            regs[instr[4]] = 0

        # Inc/Dec if conditional is satisfied
        if ops[instr[5]](regs[instr[4]], int(instr[6])):
            regs[instr[0]] = ops[instr[1]](regs[instr[0]], int(instr[2]))

        # Update max
        max_val = regs[instr[0]] if regs[instr[0]] > max_val else max_val

    return max(regs.values()), max_val

with open("./input.txt") as f:
    instructions = [[x for x in line.strip().split()] for line in f]
    result = ab(instructions)
    print("a: {}".format(result[0]))
    print("b: {}".format(result[1]))
