def flipAndInvertImage(image):
    for el in image:
        l, r = 0, len(el) - 1
        while l <= r:
            el[l], el[r] = el[r], el[l]
            el[l] = 0 if el[l] else 1
            if l != r:
                el[r] = 0 if el[r] else 1
            r -= 1
            l += 1
    return image


    # ml = []
    # for el in image:
    #     nl = []
    #     for j in el:
    #         if j == 1:
    #             j = 0
    #         else:
    #             j = 1
    #         nl.append(j)
    #     nl.reverse()
    #     ml.append(nl)
    # return ml
print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
