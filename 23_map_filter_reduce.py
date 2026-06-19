"""map"""
num  = [1, 4, 15, 34, 62]
def square(x):
    return(x**2)

square(2)

new = list(map(square, num))#The map() function applies a given function to each item of an iterable and returns an iterator that yields the results.
print(new)
##or
num  = [1, 4, 15, 34, 62]
new2 = list(map(lambda x : x**2, num))
print(new2)


"""filter"""

def no_greater_than_9(a):
    if a >= 9:
        return True
    else:
        return False
    
numbers = {45 ,1, 5, 85, 34, 21, 7, 66, 8, 2, 44}
greater_than_9 = list(filter(no_greater_than_9, numbers))#The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.
print(greater_than_9)
##or
numbers = {45 ,1, 5, 85, 34, 21, 7, 66, 8, 2, 44}
greater_than_9_2 = list(filter(lambda x : x>=9, numbers))
print(greater_than_9_2)


"""reduce"""
from functools import reduce

l = [1, 2, 3, 4, 5, 6]
def sum(a, b):
    return a+b
l_sum = reduce(sum, l)
print(l_sum)