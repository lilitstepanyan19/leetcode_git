def bla(x):
    if x < 0:
        return False
    num = 0
    orig = x
    while x:
        x, d = divmod(x, 10)
        num = num * 10 + d
    return num == orig


    # x = str(x)
    # if x == x[::-1]:
    #     return True
    
    # return False



print(bla(121))
print(bla(1121))










