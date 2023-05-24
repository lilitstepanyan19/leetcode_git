def repeatedSubstringPattern(s):
    x = ''
    for i in range(len(s)):
        x = s[:i]
        if len(x) != 0:
            if x * (len(s) // len(x)) == s:
                    return True
    return False

    # x = ''
    # for i in range(len(s)):
    #     x = s[:i]
    #     for j in range(1, len(s) + 1):
    #         if x * j == s:
    #             return True
    # return False

    # return s in (s + s)[1:-1]
    
print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("bb"))