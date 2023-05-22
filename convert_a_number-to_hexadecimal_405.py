def toHex(num):
    if num < 0:
        return hex(num+(1<<32))[2:]
    else:
        return hex(num)[2:]
    return 
print(toHex(26))
print(toHex(-1))