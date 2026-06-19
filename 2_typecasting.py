a = 12
print(a)
print(type(a))

b = "12"
print(b)
print(type(b))

c = int(b)
print(c)
print(type(c))

no1 = input("Enter first no.- ")
no2 = input("Enter second no.- ")

print(type(no1))
print(type(no2))
print(f"Addition before typecasting {no1} + {no2} = {no1 + no2}")
print(f"Addition after typecasting {no1} + {no2} = {int(no1) + int(no2)}")