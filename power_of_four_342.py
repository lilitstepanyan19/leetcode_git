def isPowerOfFour(n):
    if n < 1:
            return False
    if n == 1:
            return True

    return isPowerOfFour(n / 4)
    # for i in range(n):
    #     if 4 ** i == n:
    #         return True

    # return False

print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))