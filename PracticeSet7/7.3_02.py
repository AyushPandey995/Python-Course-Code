class MathUtils():

    
    @staticmethod
    def add(a, b):
        return f"Addition of {a} and {b} is {a+b}"

    @classmethod
    def description(cls):
         print("This is a utility class for math operations.")

print(MathUtils.add(13, 5))
MathUtils.description()