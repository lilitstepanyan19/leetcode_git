def maximumValue(strs):
    x = []
    for el in strs:
        c = 0
        if el.isdigit():
            c = int(el)
        else:
            c = len(el)
        x.append(c)       
            
    return max(x)
print(maximumValue(["alic3","bob","3","4","00000"]))
print(maximumValue(["1","01","001","0001"]))
