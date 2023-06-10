def nextGreaterElement(nums1, nums2):
    ml = []
    for i in range(len(nums1)):
        for j in range(len(nums2) - 1):
            if nums1[i] == nums2[j]:
                k = j
                while k < len(nums2):
                    if nums2[j] < nums2[k]:
                        ml.append(nums2[k])
                        break
                    k += 1
                else:
                    ml.append(-1)
        if nums1[i] == nums2[-1]:
            ml.append(-1)
    return ml
print(nextGreaterElement([4,1,2], [1,3,4,2]))
print(nextGreaterElement([2,4], [1,2,3,4]))