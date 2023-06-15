def findLUSlength(a, b):
    c = ''
    x = ''
    z = ''
    if a == b:
        return -1
    if len(a) <= len(b):
        x = a
        z = b
    else:
        x = b
        z = a
    for i in range(len(x) - 1):
        for j in range(i, len(z) - 1):
            if x[i] == z[j] and x[i + 1] == z[j]:
                c += x[i]
    if c != z:
        return len(z)
    return -1
print(findLUSlength("aba", "cdc"))
print(findLUSlength("aaa", "bbb"))
print(findLUSlength("aaa", "aaa"))
print(findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))