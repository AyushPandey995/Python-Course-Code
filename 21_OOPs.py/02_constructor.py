class employee:

    def __init__(self, name , salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    
    def info(self):
        return f"Name of the employee is {self.name}. For {self.bond} years of bond will get {self.salary} as salary."


e1 = employee("Karan", 600000, 4)
print(e1.info())

e2 = employee(5000000, "Ayush", 7)
print(e2.info())

"""WE CAN GIVE DEFAULT VALUES WHICH HELPS WHEN VALUE IS NOT ASSIGNED"""

class employee:

    def __init__(self, name = "Unknown" , salary = "400000", bond = 3):
        self.name = name
        self.salary = salary
        self.bond = bond
    
    def info(self):
        return f"Name of the employee is {self.name}. For {self.bond} years of bond will get {self.salary} as salary."


e1 = employee("Karan")
print(e1.info())

e2 = employee(salary = 544400)
print(e2.info())
