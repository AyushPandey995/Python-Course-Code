from time import time
def decorator(func):
    def wrapper(n):
        time1 = time()
        func(n)
        time2 = time()
        print(time2-time1)
    return wrapper

@decorator
def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(result) 

sum(1000000)
