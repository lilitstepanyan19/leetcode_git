def findNumbers(nums):
    def d_num(num):
        ret = 0
        while num:
            num //= 10
            ret += 1
        return ret
    ans = 0
    for num in nums:
        ans += 0 if d_num(num) % 2 else 1
    return ans

    # c = 0
    # for num in nums:
    #     x = 0
    #     for el in str(num):
    #         x += 1
    #     if x % 2 == 0:
    #         c += 1
    # return c
print(findNumbers([12,345,2,6,7896]))
print(findNumbers([555,901,482,1771]))