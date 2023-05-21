def containsNearbyDuplicate(nums, k):
    if len(set(nums)) == len(nums):
            return False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(i - j) <= k:
                if nums[i] == nums[j]:
                    return True
    return False
print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))