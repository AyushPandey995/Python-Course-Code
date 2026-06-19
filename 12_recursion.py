### Easy example of Recursion
def show(n):
    if n == 0 : #Base case... Used to stop the execution at a point
        return 
    else:
        print(n)
        show(n-1)
   
show(5)

## Solving Fibonacci Series
"""
series - 0  1  1  2  3  5  8  13 ....
index -  0  1  2  3  4  5  6  7  ....
"""
def fib(n):
    if (n == 0 or n == 1):  ## This is the base case. I we not use the base case the program may go for infinite execution.
        return n
    else:
        return fib(n-2) + fib(n-1)
    
print(fib(6))

 #other example
def factorial(n):
    if( n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)  

print(factorial(4)) 