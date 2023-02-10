def romanToInt(s):
    val_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(s)):
        if i > 0 and val_dict[s[i]] > val_dict[s[i - 1]]:
            sum += val_dict[s[i]] - 2 * val_dict[s[i - 1]]
        else:
            sum += val_dict[s[i]]
    return sum


print(romanToInt('MCMXCIV'))
print(romanToInt('III'))
print(romanToInt('LIV'))

