class Employee():
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self): #used by normal users
        return f"The name is {self.name} and salary is {self.salary}"
    
    def __repr__(self): #mainly used by developers
        return f"name: {self.name} \nsalary: {self.salary}"
    
    def __len__(self): #used to return length of any thing
        return len(self.name)

e1 = Employee("Ayush", 5000000)
print(str(e1))
print(repr(e1))
print(len(e1))