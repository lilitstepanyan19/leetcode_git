def findMaxConsecutiveOnes(nums):
    ml = 0
    s = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            s += 1
        else:        
            ml = max(ml, s)
            s = 0
    return max(s, ml)
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))