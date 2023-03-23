def distinctAverages(nums):
    c = []
    while nums:
        a = max(nums)
        b = min(nums)
        if not (a + b) / 2 in c:
            c.append((a + b) / 2)
        nums.remove(a)
        nums.remove(b)
    return len(c)
print(distinctAverages([4,1,4,0,3,5]))
print(distinctAverages([1,100]))
print(distinctAverages([9,5,7,8,7,9,8,2,0,7]))