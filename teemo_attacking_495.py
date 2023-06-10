def findPoisonedDuration(timeSeries, duration):
    c = 0
    for i in range(1, len(timeSeries)):
        if timeSeries[i] > timeSeries[i - 1] + duration - 1:
            c += duration
        else:
            c += timeSeries[i] - timeSeries[i - 1]
    return c + duration
print(findPoisonedDuration([1,4], 2))
print(findPoisonedDuration([1,2], 2))
print(findPoisonedDuration([1,2,3,4,5,6,7,8,9], 1000000))