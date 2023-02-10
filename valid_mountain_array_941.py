def validMountainArray(arr):

    i = 0
    j = len(arr) - 1 
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    while j > 0 and arr[j - 1] > arr[j]:
        j -= 1
    return i == j and 0 < i < len(arr) - 1
    # if len(arr) < 3:
    #     return False
    # for i in range(1, len(arr) - 1):
    #     if arr[i - 1] > arr[i] or arr[i] < arr[i + 1]:
    #         return False
    #     if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
    #         return True
    # return False

print(validMountainArray([2,1]))
print(validMountainArray([3,5,5]))
print(validMountainArray([0,3,2,1]))
print(validMountainArray([3,7,6,4,3,0,1,0]))
print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))