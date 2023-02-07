def countBits(n):
    ans = []
    for i in range(n+1):
        c = 0
        while i:
            c += i % 2
            i >>= 1
        ans.append(c)
        
    return ans

print(countBits(2))
print(countBits(5))