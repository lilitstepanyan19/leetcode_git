def isSubsequence(s, t):
    ml = list(s)
    for el in t:
        if ml[0] == el:
            ml.pop(0)
    return len(ml) == 0
    
    # if s == '':
    #     return True
    # ml = []

    # for el in t:
    #     if el in s:
    #         if el not in ml:
    #             ml.append(el)

    # if len(s) == len(ml):
    #     if ''.join(ml) == s or ''.join(ml)[::-1] == s:    
    #         return True

    # return False

print(isSubsequence("ab", "baab"))
print(isSubsequence("axc", "ahbgdc"))