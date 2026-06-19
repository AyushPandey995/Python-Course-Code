a = (3, 47, 2, 81, 51, 14)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

b = (5, ) #way to write single element tuple
print(b)

"""tuple unpacking"""
new = (12, 87, 55544)
a, b, c = new
print(a)
print(a, b, c)

num = (1, 32, 77, 2, 1, 84, 77, 2, 58, 29, 77)
print(num.count(77))
print(num.index(77)) ## gives the index of first occurance of that element


