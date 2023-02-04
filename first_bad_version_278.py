def firstBadVersion(n):
    l, r = 1, n
    # while l <= r:
    #     m = (l + r) // 2
    #     if isBadVersion(m):
    #         r = m -1
    #     else:
    #         l = m + 1
    return l

print(firstBadVersion(5))
print(firstBadVersion(1))