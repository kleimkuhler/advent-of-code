def a(A):
    sum = 0
    for phrase in A:
        s = set(phrase)
        if len(phrase) == len(s):
            sum += 1
    return sum

def b(A):
    sum = 0
    for phrase in A:
        phrase = [''.join(sorted(word)) for word in phrase]
        s = set(phrase)
        if len(phrase) == len(s):
            sum += 1
    return sum

with open("./input.txt") as f:
    passphrases = [[x for x in line.strip().split()] for line in f]
    print("a: {}".format(a(passphrases)))
    print("b: {}".format(b(passphrases)))
