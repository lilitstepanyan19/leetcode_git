def longestCommonPrefix(strs):
    ml = ''
    mw = min(strs)
    for i in range(len(mw)):
        for el in strs:
            if ml == len(el) or el[i] != mw[i]:
                return ml
        ml += strs[0][i]
    return ml

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["aac","a","ccc"]))
print(longestCommonPrefix(["ab","a"]))
   