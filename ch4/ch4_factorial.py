def factorial(num):
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(2))
print(factorial(0))
print(factorial(1))
print(factorial(5))
