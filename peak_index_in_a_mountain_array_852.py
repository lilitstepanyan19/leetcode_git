def peakIndexInMountainArray(arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            l = arr[mid]
        else:
            r = arr[mid]
    # for i in range(len(arr)-1):
    #     if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
    #         return i

    return 

print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))