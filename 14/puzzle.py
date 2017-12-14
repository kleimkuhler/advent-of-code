from knot_hash import compute, dense

cat = ''.join
grid = []

def knot_hash(keystring):
    asciistring = [ord(x) for x in keystring] + [17, 31, 73, 47, 23]
    return dense(compute(asciistring, 64))

def walk_disk(keystring):
    for i in range(128):
        knothash = knot_hash('{}-{}'.format(keystring, i))
        bitstring = cat(map('{0:04b}'.format, [int(x, 16) for x in knothash]))
        grid.append([b for b in bitstring])
        yield bitstring

def defragment(keystring):
    return sum(sum([int(x, 2) for x in row]) for row in walk_disk(keystring))

def regions():
    count = 0
    nodes = [(i, j) for i in range(128) for j in range(128) if grid[i][j] == '1']
    while nodes:
        visited = [nodes[0]]
        while visited:
            (x, y) = visited.pop()
            if (x, y) in nodes:
                nodes.remove((x, y))
                visited += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        count += 1
    return count

with open('./input.txt') as f:
    keystring = f.readline().strip()
    print('1: {}'.format(defragment(keystring)))
    print('2: {}'.format(regions()))
