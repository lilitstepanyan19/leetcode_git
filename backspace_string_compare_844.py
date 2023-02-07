def backspaceCompare(s, t):
    def x(s):
        m = []
        for el in s:
            if el == '#':
                if m:
                    m.pop()
            else:
                m.append(el)
        return ''.join(m)
    return x(s) == x(t)

    # def x(s):
    #     m = []
    #     for el in s:
    #         if m and el == '#':
    #             m.pop()
    #         elif el != '#':
    #             m.append(el)
    #     return m    
    # return x(s) == x(t)

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))
print(backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz", "oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"))

