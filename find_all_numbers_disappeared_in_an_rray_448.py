def findDisappearedNumbers(nums):

    return set(range(1, len(nums) + 1)) - set(nums)

    # n = len(nums) + 1
    # ml = []
    # for i in range(1, n):
    #     if i not in set(nums):
    #         ml.append(i)
    # return ml

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))