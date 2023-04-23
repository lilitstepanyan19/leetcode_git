def isValid(s):
    l = ['(', '{', '[']
    r = [')', '}', ']']
    ml = []
    for el in s:
        if el in l:
            ml.append(el)
        else:
            if not ml or l.index(ml[-1]) != r.index(el):
                return False
            else:
                ml.pop()
    return not ml 

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(}{)"))
print(isValid("{[]}"))
print(isValid("){"))