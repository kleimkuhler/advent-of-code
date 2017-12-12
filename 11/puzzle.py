origin = (0, 0)

# https://www.redblobgames.com/grids/hexagons/#neighbors-axial
axial_coordinates = dict(
    n = (0, -1), ne = (1, -1), se = (1, 0),
    s = (0, 1), sw = (-1, 1), nw = (-1, 0),
)

def axial_distance(path):
    x, y = origin
    furthest = 0
    for (dx, dy) in map(axial_coordinates.get, path):
        x += dx; y += dy
        furthest = max(furthest, x, y)
    distance = (abs(x) + abs(y) + abs(x + y)) // 2
    return (distance, furthest)

with open('./input.txt') as f:
    path = f.readline().strip().split(',')
    followed = axial_distance(path)
    print('1: {}'.format(followed[0]))
    print('2: {}'.format(followed[1]))
