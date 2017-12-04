import itertools

def a(A):
    sum = 0
    for row in A:
        sum += max(row) - min(row)
    return sum

def b(A):
    sum = 0
    for row in A:
        for a, b in itertools.combinations(row, 2):
            if a % b == 0 or b % a == 0:
                sum += a // b + b // a
    return sum

with open('./input.txt') as f:
    spreadsheet = [[int(x) for x in line.strip().split()] for line in f]
    print("a: {}".format(a(spreadsheet)))
    print("b: {}".format(b(spreadsheet)))
