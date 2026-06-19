# del keyword
class Student():

    college = "SAOE"

    def __init__(self, name, age):
        self.name = name
        self.age = age 

s1 = Student("Lalit", 23)
print(s1.college)
print(s1.name) 
print(s1.age)

# del(s1)

# print(s1) # -> this will throw an error

""" We can directly change the values of attributes """
s1.name = "mahi"
print(s1.name)  


