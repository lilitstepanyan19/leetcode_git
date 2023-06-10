import math


def constructRectangle(area):
    l = w = int(math.sqrt(area))
    while l * w != area:
        if l * w < area:
            l += 1
        else:
            w -= 1
    return [l, w]
print(constructRectangle(4))
print(constructRectangle(37))
print(constructRectangle(122122))