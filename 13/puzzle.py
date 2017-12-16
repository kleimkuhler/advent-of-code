import re

from itertools import count

caught  = lambda layer, height: layer % ((height - 1) * 2) == 0
compute = lambda firewall: \
          sum(l*h for l, h in firewall.items() if caught(l, h))
wait    = lambda firewall: \
          next(delay for delay in count() \
               if not any(caught(l+delay, h) for l, h in firewall.items()))

with open('./input.txt') as f:
    firewall = {}
    for line in f:
        layer, height = re.findall(r'\d+', line)
        firewall[int(layer)] = int(height)
    print('1: {}'.format(compute(firewall)))
    print('2: {}'.format(wait(firewall)))
