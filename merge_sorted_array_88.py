def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))



# def merge(nums1, m, nums2, n):
    # nums1 = nums1[:m] + nums2
    # nums1.sort()
    # return nums1