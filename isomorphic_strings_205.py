def isIsomorphic(s, t):
    return list(map(s.find,s)) == list(map(t.find,t))

    # for i in range( len(s)):
    #         if t[i] not in s or s[i] == t[i]:
    #             s = s.replace(s[i], t[i])   
    # if s == t:
    #     return True
    # return False
print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("babc", "baba"))
print(isIsomorphic("abab", "baba"))