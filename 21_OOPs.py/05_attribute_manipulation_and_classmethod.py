class Student():
    college = "SAOE"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg (self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"Hiii {self.name}, your average score is {sum/5}")
s1 = Student("Ayush", [95, 89, 93, 98, 91])
print(s1.marks)
s1.get_avg()

s1.name = "Kanha"
s1.get_avg()


"""@classmethod"""
class Person():
    name = "anonymous"

    def change_name(self, name):
        self.name = name

p1 = Person()
p1.change_name("Ayush")
print(p1.name)
print(Person.name)  # this show the name as "anonymous"

# ###To change the class attribute we use different methods

# #1st -> uses name of class ie. "Person" before attribute name
# class Person():
#     name = "anonymous"

#     def change_name(self, name):
#         Person.name = name

# p1 = Person()
# p1.change_name("Ayush")
# print(p1.name)
# print(Person.name)

# #2nd -> used the __class__ after self
# class Person():
#     name = "anonymous"

#     def change_name(self, name):
#         self.__class__.name = name

# p1 = Person()
# p1.change_name("Ayush")
# print(p1.name)
# print(Person.name)

# #3rd -> used the @classmethod 
# class Person():
#     name = "anonymous"

#     @classmethod
#     def change_name(cls, name):
#         cls.name = name

# p1 = Person()
# p1.change_name("Ayush")
# print(p1.name)
# print(Person.name)