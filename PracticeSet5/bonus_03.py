d1 = {"Pen": 10, "Chart paper": 20}
d2 = {"Pencil": 5, "Eraser": 3}
print(d1)
print(d2)
d3 = {}
for key, value in d1.items():
    d3[key] = value
for key, value in d2.items():
    d3[key] = value

print(d3)

"""or"""

d4 = d1|d2
print(d4)
