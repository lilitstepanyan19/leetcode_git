def reverseString(s):
    l, r = 0, len(s) - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s
    # s.reverse()
    # return s

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))