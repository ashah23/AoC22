import numpy as np

grid = []
filename = "Day8\\input.txt"

with open(filename) as f:
    for line in f:
        grid.append([int(x) for x in line.strip()])

visible = []
maxX = len(grid) - 1
maxY = len(grid[0]) - 1
for x in range(len(grid)):
    lst = []
    for y in range(len(grid[0])):
        if x == 0 or y == 0 or x == maxX or y == maxY:
            lst.append(True)
        else:
            lst.append(False)
    visible.append(lst)

grid = np.array(grid)
visible = np.array(visible)


lowX = 1
lowY = 1
for x in range(lowX, maxX): 
    for y in range(lowY, maxY):

        val = grid[x][y]
        ygrid = grid[:, y]
        xgrid = grid[x, :]
        if max(ygrid[:x]) < val \
        or max(ygrid[x+1:]) < val \
        or max(xgrid[:y]) < val \
        or max(xgrid[y+1:]) < val:
            visible[x][y] = True

vis = 0
for line in visible:
    for v in line:
        if v == True:
            vis += 1

print(str(vis))
