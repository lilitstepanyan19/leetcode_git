def kidsWithCandies(candies, extraCandies):
    ml = []
    c = max(candies)
    for el in candies:
        if el + extraCandies>= c:
            ml.append('true')
        else:
            ml.append('false')
    return ml
print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))