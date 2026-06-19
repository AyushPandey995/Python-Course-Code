class animal():
    location = "India"
    def __init__(self, name):
        self.name = name
    def speak(self):
       return"generic sound"

class dog(animal):
    def speak(self):
        return "Woof!!"

class cat(animal):
    def speak (self):
        print(super().speak()) # uses the speak function of parent calss ie. class animal -> give the value of speak of animal in output of class cat
        return "Meow!!"

a = animal("Dog -> Bruno")
print(a.name)
print(a.speak())

d = dog("Bruno")
print(d.name)
print(d.speak())
print(d.location)

c = cat("Corna")
print(c.name)
print(c.speak())

# """other example"""

# class Car():
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class Toyota(Car):
#     def __init__(self, type, name):
#         super().__init__(type) # -> this is to use the class attribute of parent/base class 
#         self.name = name



# v1 = Toyota("Diesel", "Innova")
# print(v1.name)
# print(v1.type)