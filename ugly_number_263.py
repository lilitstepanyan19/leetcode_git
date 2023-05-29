def isUgly(n):

    if n <= 0:
        return False
    
    x = n
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        elif x % 3 == 0:
            x = x // 3
        elif x % 5 == 0:
            x = x // 5
        else:
            return False
    return True
print(isUgly(6))
print(isUgly(1))
print(isUgly(14))