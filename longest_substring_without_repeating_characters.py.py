def lengthOfLongestSubstring(s):
    x = []
    max_lenght = 0
    for el in s:
        if el in x:
            x = x[x.index(el) + 1:]
        x.append(el)
        max_lenght = max(len(x), max_lenght)
    return max_lenght



print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("xaxhifdzyuddj"))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("bpoiexpqhmebhhu"))














    # start = -1
    # max = 0
    # d = {}

    # for i in range(len(s)):
    #     if s[i] in d and d[s[i]] > start:
    #         start = d[s[i]]
    #         d[s[i]] = i
            
    #     else:
    #         d[s[i]] = i
    #         if i - start > max:
    #             max = i - start
    # print(d)
    # return max



