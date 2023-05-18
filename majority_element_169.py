def majorityElement(nums):
    d = {}
    for el in nums:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for k,v in d.items():
        if v > len(nums) / 2:
            return k
    return 

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,3,4]))