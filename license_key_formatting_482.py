def licenseKeyFormatting(s, k):

    s = s.replace('-', '').upper()
    ans = ''
    for i in range(len(s) - 1, -1, -1):
        if not len(ans) % (k + 1):
            ans += '-'
        ans += s[i]
    return ans[::-1][:-1]

    # for el in s:
    #     if el == '-':
    #         s = s.replace('-', '')
    # ml = ''
    # c = len(s) % k
    # if c != 0:
    #     ml = s[:c].upper() + '-'
    #     for i in range(c, len(s), k):
    #         ml += s[i:i+k].upper() + '-'
    # else:
    #     for i in range(0, len(s), k):
    #         ml += s[i:i+k].upper() + '-'

    # return ml[:-1]

print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J", 2))
