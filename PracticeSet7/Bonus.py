class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return f"{self.x + p.x}, {self.y + p.y}"
    

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1+p2)