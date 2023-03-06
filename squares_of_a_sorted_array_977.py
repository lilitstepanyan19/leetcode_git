def sortedSquares(nums):

    l, r = 0, len(nums) - 1
    ans = []
    while l <= r:
        if abs(nums[r]) > abs(nums[l]):
            ans.append(nums[r] * nums[r])
            r -= 1
        else:
            ans.append(nums[l] * nums[l])
            l += 1
    return ans[::-1]

    # ml = []
    # for el in nums:
    #     ml.append(abs(el)**2)
    # ml.sort()
    # return ml
print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))