def wordPattern(pattern, s):
    l = []
    s = s.split(' ')
    for el in s:
        l.append(s.index(el))
    return list(map(pattern.find, pattern)) == l
print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))