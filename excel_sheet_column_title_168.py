def convertToTitle(columnNumber):
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ml = ''
    while columnNumber > 0:
        ml = letter[(columnNumber - 1) % 26] + ml
        columnNumber = (columnNumber - 1) // 26

    return ml


print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(2147483647))