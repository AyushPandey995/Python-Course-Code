# class Account():
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no

#     def credit(self, value):
#         self.balance += value
#         print("Balance - ", self.balance)

#     def debit(self, value):
#         self.balance -= value
#         print("Balance - ", self.balance)

# client1 = Account(45664, 456564)
# client1.credit(30)        
# client1.debit(10)


# class Employee():

#     def __init__(self, full_name, salary):
#         self.full_name = full_name
#         self.salary = salary

#     def first_name(self):
#         l = self.full_name.split()
#         return "First name of Employee is",l[0]
    
#     def last_name(self):
#         l = self.full_name.split()
#         return "Last name of Employee is", l[-1]
    
#     def update_salary(self, sal):
#         self.salary = sal
#         print(f"Updated salary of {self.full_name} is {self.salary}")

#     def set_first_name (self, f_name):
#         self.full_name = f"{f_name} {self.last_name()}" 
#         print(f"Updated name of Employee is {self.full_name}")
    
#     def set_last_name (self, l_name):
#         self.full_name = f"{self.first_name()} {l_name}" 
#         print(f"Updated name of Employee is {self.full_name}")
    
# e1 = Employee("Jhos Der", 26564)
# print(e1.full_name)
# print(e1.salary)
# e1.update_salary(50000)
# print(e1.first_name())
# e1.set_first_name("Jhon")
# print(e1.last_name())
# e1.set_last_name("Doe")




class Employee():

    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary

    @property
    def first_name(self):
        l = self.full_name.split()
        return l[0]
    
    @property
    def last_name(self):
        l = self.full_name.split()
        return l[-1]
    
    @first_name.setter
    def first_name (self, f_name):
        self.full_name = f"{f_name} {self.last_name}" 
    
    @last_name.setter
    def last_name (self, l_name):
        self.full_name = f"{self.first_name} {l_name}" 

e1 = Employee("Jhos Der", 26564)
print(e1.full_name)
print(e1.salary)

print(e1.first_name)
e1.first_name = "Jhon"
print(e1.last_name)
e1.last_name = "Doe"
print(e1.full_name)