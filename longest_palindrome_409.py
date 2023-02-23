from collections import Counter


def longestPalindrome(s):
    ans = 0
    cnt = Counter(s)
    for l, c in cnt.items():
        cur = c - c % 2
        ans += cur
        cnt[l] += cur
    if ans == len(s):
            return ans
    return ans if not sum(cnt.values()) else ans + 1
    

    # c = 0
    # x = 0
    # d = {}
    # for el in s:
    #     if s.count(el) == len(s):
    #         return len(s)
    #     if el in d:
    #         d[el] += 1
    #     else:
    #         d[el] = 1
    # for el in d:
    #     if d[el] % 2 == 0:
    #         c += d[el] 
    #     else:
    #         c += d[el] - d[el] % 2 
    #         x += 1
    # if x >= 1:
    #     c += 1
    # return c
print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("aaa"))
print(longestPalindrome("bananas"))