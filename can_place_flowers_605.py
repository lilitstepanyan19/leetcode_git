def canPlaceFlowers(flowerbed, n):

    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed) - 1):
        if not sum(flowerbed[i - 1: i + 2]):
            flowerbed[i] = 1
            n -= 1
    if n < 1:
        return True
    return False

    # flowerbed = [0] + flowerbed + [0]
    # for i in range(1, len(flowerbed) - 1):
    #     if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
    #         flowerbed[i] = 1
    #         n -= 1
    # if n < 1:
    #     return True
    # return False

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))