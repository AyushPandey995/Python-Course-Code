# def average (a,b,c):
#     d = (a+b+c)/3
#     print(d)

# average(5,3,1)

###But here we can not assign value of average to any veriable. For that return is used. If we directly assign value of average to any veriable without using returm then "None" will get as result

##Normal Agruments
def average (a,b,c):
    d = (a+b+c)/3
    return d

a1 = average(5,3,1)
a2 = average(10,5,15)
print(a1)
print(a2)

###Default Agrumnets

def greet (name , sur_name = ""):
    return f"Have a nice day {name} {sur_name}"

print(greet("Ayush"))
print(greet("Khushi", "Pandey"))

###Keyword Arguments
def greet (name , sur_name = ""):
    return f"Have a nice day {name} {sur_name}"

print(greet(sur_name = "Pandey", name = "Ayush"))
