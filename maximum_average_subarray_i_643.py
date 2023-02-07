def findMaxAverage(nums, k):
    ans = float('-inf')
    c = 0
    cur = 0
    for i in range(len(nums)):
        cur += nums[i]
        c +=1
        if c == k:
            ans = max(ans, cur / k)
        if c > k:
            cur -= nums[i-k]
            ans = max(ans, cur / k)
    return ans
    # ans = []
    # for i in range(len(nums)):
    #     if k + i > len(nums):
    #         continue
    #     s = sum(nums[i:k+i])
    #     ans.append(s/k)

    # return max(ans)

print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))
