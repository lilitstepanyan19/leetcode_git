def isAlienSorted(words, order):
    if len(words) < 2:
        return True
    d = {c : i for i, c in enumerate(order)}
    for k in range(len(words)):
        w1 = words[k - 1]
        w2 = words[k]
        l1, l2 = len(w1), len(w2)
        i, j = 0, 0
        while i < l1 and j < l2:
            o1, o2 = d[w1[i]], d[w2[j]]
            if o1 < o2:
                return False

            i += 1
            j += 1
        if l1 > l2 and w1[:l2 + 1] == w2:
            return False
    return True

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
# print(isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
# print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))