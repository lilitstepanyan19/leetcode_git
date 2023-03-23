def applyOperations(nums):
    ml = nums
    for i in range(len(nums) - 1):
        
        if nums[i] == nums[i - 1]:
            ml[i - 1], ml[i] = ml[i] * 2, 0
        else:
            continue
    if ml[-2] == ml[-1]:
        ml[-2], ml[-1] = ml[-2] * 2, 0

    for j in range(len(nums)):
        for i in range(len(ml) - 1):
            if ml[i] == 0:
                ml[i], ml[i + 1] = ml[i + 1], ml [i]

    return ml

print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([0,1]))
print(applyOperations([2,2,4]))
print(applyOperations([2,1,1]))
print(applyOperations([312,312,436,892,0,0,528,0,686,516,0,0,0,0,0,445,445,445,445,445,445,984,984,984,0,0,0,0,\
    168,0,0,647,41,203,203,241,241,0,628,628,0,875,875,0,0,0,803,803,54,54,852,0,0,0,958,195,590,300,126,0,0,523,523]))