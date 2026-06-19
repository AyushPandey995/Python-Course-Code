coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

"""coordinates[0] = 50, this is not possible as tuples are immutable"""
print(coordinates)
tuple_list = list(coordinates)
tuple_list[0] = 50
coordinates = tuple(tuple_list)
print(coordinates)

