s = {54, 22, 13, 47, 74, 54, 8, 74}
print(s)
print(len(s))

"""Methods"""
new = {45, 71, 13, 7, 83}
new.add(15)
print(new)
new.remove(45) #Raise error if the element is not present in the set
print(new)
new.discard(1) #Does not raise any error if the element is not present in the set
print(new)
print(new.pop()) #remove some random element from the set

"""set operations"""
a = {1,2,3,5,6}
b = {4,5,6,7,8}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)
f = b.difference(a)
print(f)

empty = set()
print(type(empty))