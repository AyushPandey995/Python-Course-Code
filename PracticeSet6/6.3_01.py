class animal():
    def sound(self):
        print("Some sound")

class dog(animal):
    def sound(self):
        print("bark")

a = animal()
a.sound()

d = dog()
d.sound() 