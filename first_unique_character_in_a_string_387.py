from collections import Counter


def firstUniqChar(s):

    cnt = Counter(s)
    for i, c in enumerate(s):
        if cnt[c] == 1:
            return i
    return -1    

    # for i in range(len(s)):
    #     if s.count(s[i]) == 1:
    #         return i
    # return -1
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))