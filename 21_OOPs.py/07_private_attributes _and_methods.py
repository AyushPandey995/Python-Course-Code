""" We put double underscore '__' in front of any attribute or method to make it private """
class Account():
    bank_name = "IDBI"

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


a1  = Account(12345, "abcde")
print(a1.acc_no)
# print(a1.__acc_pass) #-> this will throw an error

a1.acc_no = 46545
print(a1.acc_no)
a1.reset_pass()


"""private method"""

class Person():

    name = "anonymous"

    def __hello(self):
        print("hello", self.name)

    def greet(self):
        self.__hello()

p1 = Person()
# p1.__hello() # -> Will throw an error
p1.greet()