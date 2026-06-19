class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
    def show(self):
        print((self.x, self.y))

p1 = point(3, 6)
p2 = point(4, 8)

p3 = p1.sum(p2)
p3.show()