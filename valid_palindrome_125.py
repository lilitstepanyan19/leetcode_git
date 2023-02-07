def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
    # ml = ''
    # for el in s:
    #     if el.isalnum():
    #         ml += el.lower()
    # if ml == ml[::-1]:
    #     return True
    # return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))