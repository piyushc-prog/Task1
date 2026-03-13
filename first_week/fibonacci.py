def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

num = int(input('please Enter the number'))
for value in fibonacci(num):
    print(value)