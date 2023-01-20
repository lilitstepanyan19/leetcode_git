def longestCommonPrefix(strs):
    c = 1
    
    for i in range(len(strs[0])):
        m = strs[0]
        if m in strs[1:i]:
            c += 1
            print(m)
     
            m = strs[0][:-i]
            print(m)
    if c == len(strs):
        return m, c

    return 'x', c

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
