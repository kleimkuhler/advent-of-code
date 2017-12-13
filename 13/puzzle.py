import re

def compute(firewall):
    severity = 0
    for layer, height in firewall.items():
        if layer % ((height - 1) * 2) == 0:
            severity += layer * height
    return severity

with open('./input_test.txt') as f:
    firewall = {}
    for line in f:
        layer, height = re.findall(r'\d+', line)
        firewall[int(layer)] = int(height)
    print('1: {}'.format(compute(firewall)))
