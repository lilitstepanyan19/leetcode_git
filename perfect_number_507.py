import math

def checkPerfectNumber(num):
    c = 1
    if num == 1:
        return False
    max = math.ceil(num**0.5)

    for i in range(2, max):
        if num % i == 0:
            c += i + num / i
    return c == num
print(checkPerfectNumber(28))
print(checkPerfectNumber(7))