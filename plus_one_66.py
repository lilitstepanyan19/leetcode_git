def plusOne(digits):
    c = 1
    for i in range(len(digits)-1, -1, -1):
        c, digits[i] = divmod(digits[i] + c, 10)
    return digits if not c else [c] + digits

    # x = ''
    # y = 0
    # for el in digits:
    #     x += str(el)
    # y = int(x) + 1
    # c = y
    # s = []
    # while c:
    #     c, d = divmod(y, 10)
    #     s.append(d)
    #     y = c
    # ans = s[::-1]
    # return ans

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))