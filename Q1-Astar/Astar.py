import Node


def aStar(start, goal, grid):
    openset = set()
    closedset = set()
    current = start
    openset.add(current)
    while openset:
        current = min(openset, key=lambda o: o.G + o.H)
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        openset.remove(current)
        closedset.add(current)
        for node in children(current, grid):
            if node in closedset:
                continue
            if node in openset:
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    node.G = new_g
                    node.parent = current
            else:
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                node.parent = current
                openset.add(node)
    raise ValueError('No Path Found')


def manhattan(point, point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1] - point2.point[0])


def children(point, grid):
    x, y = point.point
    links = [grid[d[0]][d[1]] for d in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]]
    return [link for link in links if link.value != '%']


def next_move(pacman, food, grid):
    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            grid[x][y] = Node(grid[x][y], (x, y))
        path = aStar(grid[pacman[0]][pacman[1]], grid[food[0]][food[1]], grid)
        print len(path) - 1
    for node in path:
        x, y = node.point
        print x, y


pacman_x, pacman_y = [int(i) for i in raw_input().strip().split()]
food_x, food_y = [int(i) for i in raw_input().strip().split()]
x, y = [int(i) for i in raw_input().strip().split()]

grid = []
for i in xrange(0, x):
    grid.append(list(raw_input().strip()))

next_move((pacman_x, pacman_y), (food_x, food_y), grid)
