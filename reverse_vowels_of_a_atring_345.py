def reverseVowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    l, r = 0, len(s) - 1
    s = list(s)
    while l <= r:
        if s[l].lower() not in v:
            l += 1
            continue
        if s[r].lower() not in v:
            r -= 1
            continue
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1       
    return ''.join(s)
print(reverseVowels("hello"))
print(reverseVowels("leetcode"))