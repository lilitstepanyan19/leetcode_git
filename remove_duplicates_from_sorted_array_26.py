def removeDuplicates(nums):

    unique_count = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            # nums[unique_count] = nums[i]
            # print(nums[unique_count],nums[i-1] ,nums[i], i)
            unique_count += 1
    return unique_count, nums
    # k = 0
    # for i in range(len(nums) - 1):
    #     if nums[i] in nums[:i] or nums[i] in nums[i+1:]:
    #         nums[i] = '_'
    # # for j in range(len(nums) - 1):
    # #     for i in range(len(nums) - 1):
    # #         if nums[i] == '_':
    # #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
    # for i in range(len(nums)):
    #     if nums[i] != '_':
    #         k += 1
    # return k, nums
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))




    # s = list(set(nums))
    # k = len(s)
    # for i in range(len(nums)):
    #     if len(s) < len(nums):
    #         s.append('_')
    # return k, s