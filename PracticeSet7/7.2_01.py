class Employee():
    def __init__(self, salary):
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value<0:
            print("Plzzz.. dont enter negative value for salary")
        else:
            self.__salary = value
e = Employee(3000000)
print(e.salary)
e.salary = 4000000
print(e.salary)

