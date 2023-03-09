def fib(n):
    f = [0, 1, 1]
    if n <= 2:
        return f[n]
    
    print(fib(n-1) , fib(n-2))
    return fib(n-1) + fib(n-2)
print(fib(2))
print(fib(3))
print(fib(4))