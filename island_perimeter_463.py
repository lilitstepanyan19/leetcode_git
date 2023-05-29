def islandPerimeter(grid):
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                x += 4
                if i > 0 and grid[i - 1][j]:
                    x -= 2
                if j > 0 and grid[i][j - 1]:
                    x -= 2
    return x
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(islandPerimeter([[1]]))
print(islandPerimeter([[1,0]]))