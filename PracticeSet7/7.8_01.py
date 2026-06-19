def sum (*args):
    total = 0
    for n in args:
        total += n
    return total

a = sum(1, 2, 3, 4, 4, 6, 7, 8, 9, 10)
print(a)

# from functools import reduce
# def sum(a, b):
#     return a+b
# list1 = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10]
# print(reduce(sum, list1))