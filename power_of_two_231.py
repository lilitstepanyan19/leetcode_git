def isPowerOfTwo(n):
    i = 0
    while i <= n/2:
        x = 2 ** i
        if x == n:
            return True
        if x > n:
            return False
        i += 1
    return False
    
    
    
    
#     if n < 1:
#             return False
#     if n == 1:
#             return True
#     return isPowerOfTwo(n/2)

    # x = n / 2
    # for i in range(int(x)):
    #     if 2 ** i == n:
    #         return True
    # return False

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
print(isPowerOfTwo(65537))