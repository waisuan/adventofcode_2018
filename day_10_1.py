import re


class Point:
    def __init__(self, x, y, incX, incY):
        self.x = int(x)
        self.y = int(y)
        self.incX = int(incX)
        self.incY = int(incY)


p = re.compile(
    'position=<\s*([-]?\d+),\s*([-]?\d+)> velocity=<\s*([-]?\d+),\s*([-]?\d+)>')
points = []

def _print():
    for p in points:
        p.x -= p.incX
        p.y -= p.incY
    # width = max(p.x for p in points) - min(p.x for p in points) + 1
    # height = max(p.y for p in points) - min(p.y for p in points) + 1
    grid = [['.' for x in range(max(p.x for p in points) + 1)]
            for y in range(max(p.y for p in points) + 1)]
    for p in points:
        print("Y:{}, X:{}".format(p.y, p.x))
        grid[p.y][p.x] = '#'
    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in grid]))

def _area():
    maxX = max(p.x for p in points)
    minX = min(p.x for p in points)
    maxY = max(p.y for p in points)
    minY = min(p.y for p in points)
    width = maxX - minX + 1
    height = maxY - minY + 1
    print("W:{}, H:{}".format(width, height))
    area = (width) * (height)
    print("Area:: {}".format(area))
    return area
    

with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        matches = p.search(line)
        if matches:
            points.append(Point(matches.group(1), matches.group(2), matches.group(3), matches.group(4)))
    prevSize = _area()
    done = False
    time = 1
    while done is not True:
        print("Tick...{}".format(time))
        for p in points:
            p.x += p.incX
            p.y += p.incY
        size = _area()
        if size > prevSize:
            done = True
        else:
            time += 1
            prevSize = size
    _print()
