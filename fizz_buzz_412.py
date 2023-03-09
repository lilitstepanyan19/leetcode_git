def fizzBuzz(n):
    ml = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ml.append('FizzBuzz')
        elif i % 3 == 0:
            ml.append("Fizz")
        elif i % 5 == 0:
            ml.append('Buzz')
        else:
            ml.append(str(i))
    return ml
print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))