# def decorator(func):
#     def wrapper():
#         print("Trying to print Hello")
#         func()
#         print("Hello is printed")
#     return wrapper

# def hello():
#     print("Hello!!")

# a1 = decorator(hello)
# a1()


# """We can also use '@decorator' to do same thing"""
# def decorator(func):
#     def wrapper():
#         print("Trying to print Hello")
#         func()
#         print("Hello is printed")
#     return wrapper

# @decorator
# def hello():
#     print("Hello!!")

# hello()

#Eg

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@uppercase
@exclaim
def hii():
    return "Hello"

print(hii())



"""Decorator with arguments"""

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                print("Hello is printing... ")
                func(a)
                print("Hello is printed")
        return wrapper
    return decorator

@repeat(7)
def hey(a):
    print(f"Hello {a}")

hey("Ayush")

