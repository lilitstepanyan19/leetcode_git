from collections import Counter


def kSmallestPairs(nums1, nums2, k):
    
    ml = {}
    nl = []
    for i in nums1:
        for j in nums2:
            ml[f'{i} + {j}'] = i + j
    cnt = Counter(ml)
    for el in cnt:
        el = el.split(' + ')
        x = []
        for i in el:
            x.append(int(i))
        nl.append(x)
    return nl[:k]
print(kSmallestPairs([1,7,11], [2,4,6], 3))
print(kSmallestPairs([1,1,2], [1,2,3], 2))
print(kSmallestPairs([1,2], [3], 3))