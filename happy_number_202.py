def isHappy(n):
    c = n
    s = []
    while n not in s:
        c = 0
        for el in str(n):
            c += int(el)**2
        s.append(n)
        if c != 1:
            n = c
        else:
            return True
    return False
print(isHappy(19))
print(isHappy(2))
print(isHappy(7))