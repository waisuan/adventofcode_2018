import re

grid = []
for i in range(0, 1500):
    grid2 = []
    for j in range(0, 1500):
        grid2.append('.')
    grid.append(grid2)

p = re.compile('\D+(\d+),(\d+)\D+(\d+)x(\d+)')

with open('input.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        m = p.search(line)
        if m:
            x = int(m.group(1))
            y = int(m.group(2))
            lenX = int(m.group(3))
            lenY = int(m.group(4))
            print("{} {} {} {}".format(x, y, lenX, lenY))
            for i in range(0, lenX):
                for j in range(0, lenY):
                    if grid[x + i][y + j] == '.':
                        grid[x + i][y + j] = '#'
                    else:
                        grid[x + i][y + j] = 'X'

count = 0
for i in range(0, 1500):
    for j in range(0, 1500):
        if grid[i][j] == 'X':
            count += 1
print("{}".format(count))
