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

best_view = 0
lowX = 1
lowY = 1
for x in range(lowX, maxX): 
    for y in range(lowY, maxY):
        up = 0
        down = 0
        left = 0
        right = 0
        val = grid[x][y]
        for viewX in reversed(range(x)):
            up += 1
            if grid[viewX][y] >= val:
                break
        for viewX in range(x+1, maxX + 1):
            down += 1
            if grid[viewX][y] >= val:
                break
        for viewY in reversed(range(y)):
            left += 1
            if grid[x][viewY] >= val:
                break
        for viewY in range(y+1, maxY + 1):
            right += 1
            if grid[x][viewY] >= val:
                break
        this_score = left*up*right*down
        if this_score > best_view:
            best_view = this_score                   


print(str(best_view))