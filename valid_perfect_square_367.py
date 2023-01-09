def isPerfectSquare(num):
    if num == 1:
         return True
    l, r = 1, num // 2
    
    while l <= r:
        x = (l + r) // 2
        sq = x * x
        if sq == num:
            return True
        if sq < num:
            l = x + 1
        else:
            r = x - 1
    return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))