def bla(x):
    if x < 0:
        return False

    x = str(x)
    if x == x[::-1]:
        return True
    
    return False



print(bla(121))
print(bla(1121))










