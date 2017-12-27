a = b = c = d = e = f = g = h = 0

a = 1
b = 99
c = b
if a != 0:
    b = b * 100 + 100000
    c = b + 17000
while True:
    f = 1
    d = 2
    while True:
        if b % d == 0:
            f = 0
        d += 1
        g = d - b
        if g == 0:
            break
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        break
    b += 17
print('2: {}'.format(h))
