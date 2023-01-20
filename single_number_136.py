def singleNumber(nums):
    ml = 0
    for el in nums:
        ml ^= el

    
    return ml

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))