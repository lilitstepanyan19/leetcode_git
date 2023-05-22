def intersect(nums1, nums2):
    ml = []
    if len(nums1) <= len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                ml.append(nums1[i])
    else:
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                nums1.remove(nums2[i])
                ml.append(nums2[i])
    return ml
print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))
print(intersect([2,1], [1,2])) 