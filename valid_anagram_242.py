from collections import Counter


def isAnagram(s, t):

    return sorted(s) == sorted(t)

    # return Counter(s) == Counter(t)


    # ml = ''
    # s = list(s)
    # x = list(t)
    # if len(s) != len(t):
    #     return False
    # for el in s:
    #     if el in x:
    #         x.remove(el)
    #         ml += el
    # if len(ml) == len(t):
    #     return True
    # return False

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))