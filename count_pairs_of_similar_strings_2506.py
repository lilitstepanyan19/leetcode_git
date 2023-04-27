def similarPairs(words):
    w = []
    c = 0
    for el in words:
        word = []
        for i in el:
            if i not in word:
                word.append(i)
        word.sort()
        w.append(word)
    
    for i in range(len(words) - 1):
        s = w[i]
        for j in range(i + 1, len(words)):
            if s == w[j]:
                print(w[j])
                c += 1
        s = w[i + 1]
    return c
    
print(similarPairs(["aba","aabb","abcd","bac","aabc"]))
print(similarPairs(["aabb","ab","ba"]))
print(similarPairs(["nba","cba","dba"]))