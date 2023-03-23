def unequalTriplets(nums):
    c = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    c += 1
    return c
print(unequalTriplets([4,4,2,4,3]))
print(unequalTriplets([1,1,1,1,1]))
print(unequalTriplets([1,2,3]))