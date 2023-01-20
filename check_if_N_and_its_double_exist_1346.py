def checkIfExist(arr):
    s = set()
    for el in arr:
        if el * 2 in s or el / 2 in s:
            return True
        s.add(el)
    return False

    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if i != j and (0 <= i and j < len(arr)) and arr[i] == 2 * arr[j]:
    #             return True
    # return False

print(checkIfExist([10,2,5,3]))
print(checkIfExist([3,1,7,11]))