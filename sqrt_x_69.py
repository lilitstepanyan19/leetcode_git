def mySqrt(x):
    l, r = 1, x // 2
    while l <= r:
        mid = (l + r) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq > x:
            r = mid - 1
        else:
            l = mid + 1   
    if x == 1:
        return 1    
    return r

print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(3))
print(mySqrt(5))