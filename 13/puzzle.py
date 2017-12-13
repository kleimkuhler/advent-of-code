import re

caught = lambda layer, height: layer % ((height - 1) * 2) == 0

def compute(firewall):
    return sum(l*h for l, h in firewall.items() if caught(l, h))

def wait(firewall):
    delay = 0
    while (any(caught(l+delay, h) for l, h in firewall.items())):
        delay += 1
    return delay

with open('./input.txt') as f:
    firewall = {}
    for line in f:
        layer, height = re.findall(r'\d+', line)
        firewall[int(layer)] = int(height)
    print('1: {}'.format(compute(firewall)))
    print('2: {}'.format(wait(firewall)))
