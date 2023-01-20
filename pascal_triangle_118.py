def generate(numRows):
    ml = [[1], [1,1]]
    if numRows < 3:
        return ml[:numRows]
    for _ in range(2,numRows):
        nl = [1]
        for j in range(1, len(ml[-1])):
            nl.append(ml[-1][j] + ml[-1][j-1])
        nl += [1]
        ml.append(nl)
    return ml

print(generate(5))
print(generate(1))