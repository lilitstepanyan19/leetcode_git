def addDigits(num):
    while num >= 10:
        cur = num
        x = 0
        while cur:
            cur, d = divmod(cur, 10)
            x += d
            print(num, cur, x)
        num = x
        
    return num

    # res = 0
    # for el in str(num):
    #     res += int(el)
    #     if res >= 10:
    #         c = 0
    #         for el in str(res):
    #             c +=  int(el)
    #         res = c
    # return res

print(addDigits(38))
print(addDigits(708538619))