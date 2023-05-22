def intersection(nums1, nums2):
    ml = []
    if len(nums1) <= len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in ml:
                ml.append(nums1[i])
    else:
        for i in range(len(nums2)):
            if nums2[i] in nums1 and nums2[i] not in ml:
                ml.append(nums2[i])
    return ml
print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))