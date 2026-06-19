def sum(a,b):
    return a+b
print(sum(2, 32))

"""using args, *args collects any extra positional arguments passed to a function into a tuple"""
def sum_no(*args):
    total = 0
    for item in args:
        total += item
    return total
print(sum_no(1, 2, 3, 4, 5, 6))


"""using kwargs"""
def view(**kwargs):
    for key, value in kwargs.items():
        print(f"Marks of {key} is {value}")
view(Ayush = 94, Khushi = 97, Kanha = 91, Shraddha = 93 )

"""combination of args and kwargs """
def see(*args, **kwargs):
    print(args)
    print(kwargs)
see(454, 552, 4, 81, udit = 747, naik = 989)