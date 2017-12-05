def a(A):
    B = A[:]
    offset = 0
    count = 0
    while offset >= 0 and offset < len(B):
        old = offset
        offset += B[offset]
        B[old] += 1
        count += 1
    return count

def b(A):
    B = A[:]
    offset = 0
    count = 0
    while offset >= 0 and offset < len(B):
        old = offset
        offset += B[offset]
        B[old] += (-1 if B[old] >= 3 else 1)
        count += 1
    return count    

with open("./input.txt") as f:
    offsets = [int(line.strip()) for line in f]
    print("a: {}".format(a(offsets)))
    print("b: {}".format(b(offsets)))
