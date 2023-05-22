def isPowerOfFour(n):
        # return n & (n-1) == 0 and n % 3 == 1
    if n == 1 or n == 4:
            return True
    for i in range(2, int(n / 4)):
        if 4 ** i == n:
            return True
        if 4 ** i > n:
            return False
    return False

print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
print(isPowerOfFour(129140162))

#     if n < 1:
#             return False
#     if n == 1:
#             return True
#     return isPowerOfFour(n / 4)

    # for i in range(n):
    #     if 4 ** i == n:
    #         return True

    # return False

