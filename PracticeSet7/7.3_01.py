class MathUtils():

    
    @staticmethod
    def add(a, b):
        return f"Addition of {a} and {b} is {a+b}"

    @classmethod
    def description(cls):
         print("This is a utility class for math operations.")

a = MathUtils
a1 = a.add(12, 5)
print(a1)
a.description()
