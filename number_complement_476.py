def findComplement(num):
    x = format(num, 'b')
    y = ''
    for i in range(len(x)):
        c = ''
        if x[i] == '0':
            c = x[i].replace('0', '1')
        else:
            c = x[i].replace('1', '0')
        y += c
    return int((y), 2)
print(findComplement(5))
print(findComplement(1))