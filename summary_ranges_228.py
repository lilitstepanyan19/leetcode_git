def summaryRanges(nums):
    if not nums:
        return []
    ml = []
    c = nums[0]
    nums.append(float('inf'))
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            e = nums[i - 1]
            if e == c:
                ml.append(str(c))
            else:
                ml.append(f'{c}-{e}')
            c = nums[i]
    return ml
print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))