def sortArrayByParity(nums):

    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums 
    
    # ml = []
    # nl = []
    # for el in nums:
    #     if el % 2 == 0:
    #         ml.append(el)
    #     else:
    #         nl.append(el)
    # return ml + nl
print(sortArrayByParity([3,1,2,4]))
print(sortArrayByParity([0]))
