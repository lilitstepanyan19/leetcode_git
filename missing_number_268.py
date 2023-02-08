def missingNumber(nums):

    return list(set(range(len(nums) + 1)) - set((nums)))[0]  

    # for i in range(1, len(nums) + 1):
    #     if i not in nums:
    #         return i
    # return
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))