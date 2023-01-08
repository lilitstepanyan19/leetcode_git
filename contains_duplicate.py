def containsDuplicate(nums):

    return len(nums) != len(set(nums))
    # x = []
    # for el in nums:
    #     if el not in x:
    #         x.append(el)
    #     else:
    #         return True

    # return False



print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))