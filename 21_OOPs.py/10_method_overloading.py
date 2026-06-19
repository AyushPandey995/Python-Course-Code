class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
    def __sub__(self, p):
        return point((self.x - p.x), (self.y - p.y))
    
    def show(self):
        print((self.x, self.y))

p1 = point(3, 6)
p2 = point(4, 8)
p3 = p1+p2
p4 = p2-p1  
p3.show()
p4.show()
