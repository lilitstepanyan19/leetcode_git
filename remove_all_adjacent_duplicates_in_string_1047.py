def removeDuplicates(s):
    ml = []
    for el in s:
        if ml and ml[-1] == el:
            ml.pop()
        else:
            ml.append(el) 
    return ''.join(ml)
print(removeDuplicates("abbaca"))
print(removeDuplicates("azxxzy"))