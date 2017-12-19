UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
grid = []

def walk(grid):
    count, path, last = 0, '', None
    x, y, dir = 0, grid[0].index('|'), DOWN
    while grid[x][y] != '':
        if grid[x][y] == '+':
            dirs = [UP, RIGHT, DOWN, LEFT]
            options = [grid[x+dx][y+dy] for dx, dy in dirs]
            move = next(filter(bool, (x for x in options if x != last)))
            dir = dirs[options.index(move)]
        elif grid[x][y].isalpha():
            path += grid[x][y]
        last = grid[x][y]
        dx, dy = dir
        x += dx; y += dy
        count += 1
    return (path, count)

with open('./input.txt') as f:
    for line in f.readlines():
        grid.append([x.strip() for x in line])
    path, count = walk(grid)
    print('1: {}'.format(path))
    print('2: {}'.format(count))
