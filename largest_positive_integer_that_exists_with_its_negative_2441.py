def findMaxK(nums):
    ml = []
    for el in nums:
        if -el in nums:
            ml.append(abs(el))
    ml.sort()
    if ml:
        return ml[-1]
    return -1
print(findMaxK([-1,2,-3,3]))
print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))