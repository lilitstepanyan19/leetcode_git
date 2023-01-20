def tribonacci(n):
    ml = [0, 1, 1]
    if n < 3:
        return ml[n]
    for i in range(3, n + 1):
        ml.append(ml[i-3] + ml[i - 2] + ml[i - 1])
    return ml[-1]

print(tribonacci(5))
