class person():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    
    def print_person (self):
        print(f"My name is {self.name} and I am {self.age} years old")

p1 = person("John Doe", 35)
print(p1.name)
print(p1.age)
p1.print_person()