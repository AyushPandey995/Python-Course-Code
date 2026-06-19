# class Employee():

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def first_name(self):
#         l = self.name.split()
#         return l[0]
    
#     def last_name(self):
#         l = self.name.split()
#         return l[1]

#     def set_first_name(self, f_name):
#         new_name = f"{f_name} {self.last_name()}"
#         self.name = new_name

#     def set_last_name(self, l_name):
#         new_name = f"{self.first_name()} {l_name}"
#         self.name = new_name
        

# e1 = Employee("Josh Der", 54545)
# print(e1.name)
# print(e1.first_name())
# print(e1.last_name())

# e1.set_first_name("John")
# print(e1.first_name())
# print(e1.name)
# e1.set_last_name("Doe")
# print(e1.name)


"""using  @property decoratoe -> getters and setters"""

class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split()
        return l[0]
    
    @property
    def last_name(self):
        l = self.name.split()
        return l[1]

    @first_name.setter
    def first_name(self, f_name):
        new_name = f"{f_name} {self.last_name}"
        self.name = new_name

    @last_name.setter
    def last_name(self, l_name):
        new_name = f"{self.first_name} {l_name}"
        self.name = new_name
        

e1 = Employee("Josh Der", 54545)
print(e1.name)

print(e1.first_name)
print(e1.last_name)
e1.first_name = "John"
e1.last_name = "Doe"
print(e1.name)