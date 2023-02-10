def findContentChildren(g, s):
    g.sort()
    s.sort()
    ans = 0
    i = 0
    for c in s:
        if c >= g[i]:
            ans += 1
            i += 1

        if i == len(g):
            break
    return ans


print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))