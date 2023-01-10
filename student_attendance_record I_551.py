def checkRecord(s):

    return s.count('A') < 2 and s.count('LLL') == 0
    # l = 0
    # a = 0
    # for el in s:
    #     if el == 'A':
    #         a += 1
    #         if a == 2:
    #             return False
    #     if el == 'L':
    #         l += 1
    #         if l > 2:
    #             return False
    #     else:
    #         l = 0
    # return True



    # if s.count('A') < 2 and 'LLL' not in s:
    #         return True
    # return False

print(checkRecord("PPALLP"))
print(checkRecord("PPALLL"))