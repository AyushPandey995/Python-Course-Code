fruits = ["apple", "banana", "cherry"]

print(fruits[0])

a = fruits.index("banana")
print(a)
fruits.remove("banana")
fruits.insert(a, "orange")
print(fruits)

'''
fruits[1] = "orange"
print(fruits)
We can do this if we already know the index of element'''

print(len(fruits))
