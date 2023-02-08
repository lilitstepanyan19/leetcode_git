def hammingDistance(x, y):
    ml = 0
    while x or y:
        ml += (x & 1) != (y & 1)
        x >>= 1
        y >>= 1

    return ml

print(hammingDistance(1, 4))
print(hammingDistance(3, 1))