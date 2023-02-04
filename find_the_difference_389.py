from collections import Counter

def findTheDifference(s, t):
    return list((Counter(t) - Counter(s)).elements())[0]

    # for i in range(len(s)):
    #     if s[i] in t:
    #         t = t.replace(s[i], '', 1)
    # return t

print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))
print(findTheDifference("a", "aa"))