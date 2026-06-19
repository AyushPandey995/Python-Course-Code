class Student():
    college = "SAOE"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def principle_name():
        print("Khushi Bhise")

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
s1.principle_name()