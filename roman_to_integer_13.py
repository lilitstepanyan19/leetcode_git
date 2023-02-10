def romanToInt(s):

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            ans += d[s[i + 1]] - d[s[i]]
            i += 1

    # val_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # sum = 0
    # for i in range(len(s)):
    #     if i > 0 and val_dict[s[i]] > val_dict[s[i - 1]]:
    #         sum += val_dict[s[i]] - 2 * val_dict[s[i - 1]]
    #     else:
    #         sum += val_dict[s[i]]
    # return sum


print(romanToInt('MCMXCIV'))
print(romanToInt('III'))
print(romanToInt('LIV'))

