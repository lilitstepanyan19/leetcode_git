def titleToNumber(columnTitle):
    w = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    res = 0
    for i in range(len(columnTitle)):
        c = 0
        for j in range(len(w)):
            
            if columnTitle[i] == w[j]:
                c += j + 1
        res = res*26 + c    
    return res

# def titleToNumber(columnTitle):
#     res = 0
#     for i in range(len(columnTitle)):
#         res = res*26 + (ord(columnTitle[i]) - 64)   
#     return res

print(titleToNumber("A"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))