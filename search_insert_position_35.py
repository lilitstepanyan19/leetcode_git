import bisect

def searchInsert(nums, target):

    return bisect.bisect_left(nums, target)

    # if target < nums[0]:
    #     return 0
    # if target > nums[-1]:
    #     return len(nums)
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    #     if target not in nums and nums[i - 1] < target < nums[i]:
    #         return i
    # return

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))