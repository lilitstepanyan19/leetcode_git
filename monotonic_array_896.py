def isMonotonic(nums):

    int, doc = True, True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            doc = False
        if nums[i] < nums[i - 1]:
            int = False
    return int or doc
    # ml = []
    # nl = []
    # x = nums[0]
    # for i in range(len(nums)):
    #     if x <= nums[i]:
    #         ml.append(nums[i])
    #     if x >= nums[i]:
    #         nl.append(nums[i])
    #     x = nums[i]
    # if len(ml) == len(nums) or len(nl) == len(nums):
    #     return True
    # return False
print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))