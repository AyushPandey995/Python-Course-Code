from functools import reduce 
num = [1, 2, 3, 4]
def prod(a, b):
    return a*b
mult = reduce(prod, num)
print(mult)