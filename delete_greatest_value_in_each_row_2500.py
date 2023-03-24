def deleteGreatestValue(grid):
    c = 0
    while grid[0]:
        x = []
        for el in grid:
            x.append(max(el))
            el.remove(max(el))
        c += max(x)
    return c
print(deleteGreatestValue([[1,2,4],[3,3,1]]))
print(deleteGreatestValue([[10]]))
print(deleteGreatestValue([[35,52,74,92,25],[65,77,1,73,32],[43,68,8,100,84],[80,14,88,42,53],[98,69,64,40,60]]))
