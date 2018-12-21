import re

grid = []
for i in range(0, 1500):
    grid2 = []
    for j in range(0, 1500):
        grid2.append('.')
    grid.append(grid2)

p = re.compile('#(\d+)\D+(\d+),(\d+)\D+(\d+)x(\d+)')

overlaps = {}
seen = {}
with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        m = p.search(line)
        if m:
            id = m.group(1)
            x = int(m.group(2))
            y = int(m.group(3))
            lenX = int(m.group(4))
            lenY = int(m.group(5))
            seen[id] = 1
            # print("{} {} {} {}".format(x, y, lenX, lenY))
            for i in range(0, lenX):
                for j in range(0, lenY):
                    if grid[x + i][y + j] == '.':
                        grid[x + i][y + j] = id
                    else:
                        overlaps[grid[x + i][y + j]] = 1
                        overlaps[id] = 1
                        # grid[x + i][y + j] = 'X'

for id in seen:
    if id not in overlaps:
        print("{}".format(id))
        break