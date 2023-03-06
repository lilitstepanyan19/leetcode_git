def hammingWeight(n):
    ans = 0
    while n:
        ans += n & 1
        print(n&1)
        n >>= 1
    return ans
    # c = 0
    # for el in range(n):
    #     if el == 1:
    #         c +=1
    # return c

print(hammingWeight(100000000000000000000000000001011))
print(hammingWeight(100000000000000000000000010000000))
print(hammingWeight(11111111111111111111111111111101))