def numJewelsInStones(jewels, stones):
    jewels = set(jewels)
    c = 0
    for el in stones:
        if el in jewels:
            c += 1
    return c

    # c = 0
    # for el in stones:
    #     if el in jewels:
    #         c += 1
    # return c
print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))