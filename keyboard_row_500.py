def findWords(words):
    a = "qwertyuiop"
    b = "asdfghjkl"
    c = "zxcvbnm"
    ml = []
    for el in words:
        aw = ''
        bw = ''
        cw = ''
        for i in range(len(el)):
            if el[i].lower() in a:
                aw += el[i]
            if el[i].lower() in b:
                bw += el[i]
            if el[i].lower() in c:
                cw += el[i]
        if aw == el or bw == el or cw == el:
            ml.append(el)
    return ml
print(findWords(["Hello","Alaska","Dad","Peace"]))
print(findWords(["omk"]))
print(findWords(["adsdf","sfd"]))
print(findWords(["a","b"]))