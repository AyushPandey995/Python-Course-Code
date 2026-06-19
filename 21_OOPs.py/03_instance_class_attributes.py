class employee:
    company = "HP"

    def __init__(self, name , salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company
    
    def info(self):
        return f"Name of the employee is {self.name}. For {self.bond} years of bond will get {self.salary} as salary."


e1 = employee("Karan", 600000, 4, "Omen")
print(e1.info())
print(e1.company) ## -> Omen
print(employee.company) ## -> HP


"""  Object Introspection -> Used to find out all the instences and methods of a particular object using 'dir'   """
print(dir(e1))