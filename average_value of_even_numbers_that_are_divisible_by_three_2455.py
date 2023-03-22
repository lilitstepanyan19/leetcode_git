def averageValue(nums):
    c = []
    for el in nums:
        if el % 3 == 0 and el % 2 == 0:
            c.append(el)
    if len(c) == 0:
        return 0
    return sum(c) // len(c)
print(averageValue([1,3,6,10,12,15]))
print(averageValue([1,2,4,7,10]))