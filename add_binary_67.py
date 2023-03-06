def addBinary(a, b):
    la, lb = len(a), len(b)
    if la > lb:
        b = '0' * (la - lb) + b
    else:
        a = '0' * (lb - la) + a
    cary = 0
    ans = ''
    for i in range(len(a) - 1, -1, -1):
        d1 = int(a[i])
        d2 = int(b[i])
        cary, d = divmod(d1 + d2 + cary, 2)
        ans += str(d)
    if cary:
        ans += str(cary)
    return ans[::-1]
print(addBinary("11", "1"))
print(addBinary("1010", "1011"))