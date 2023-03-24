def pivotInteger(n):
    x = 0
    for i in range(n + 1):
        x += i
        y = 0
        for j in range(n + 1):
            y += n - j
            if x == y and i + j == n:
                return i
    return -1
print(pivotInteger(8))
print(pivotInteger(1))
print(pivotInteger(4))