# a = int(input("Enter a number: "))
# table = []

# for i in range (1, 11):
#     table.append(a*i)    
# print(table)


"""By list comprehension"""

t = [5*i for i in range(1,11)]
print(t)

square_table = [i**2 for i in range(1,11)]
print(square_table)


"""Using for and if in list comprehension"""
#Create a list of numbers which is multiple of 3 and divisible of 2 between 1 to 100
list2 = [3*i for i in range (1, 35) if ((3*i)<100) and ((3*i)%2==0) ]
print(list2)


"""Using for, if and else in list comprehension"""
list3 = ["Even" if i%2 == 0 else "Odd" for i in range (1, 30)]
print(list3)


"""Creating pairs usinf nested for loop"""
list4 = [(x, y) for x in range(2) for y in range(4)]
print(list4)

# for i in range (2):
#     for j in range(4):
#         print((i,j))


"""list comprehension with function"""
animal = ["Tiger", "Lion", "Dog", "Cat", "Cow", "Horse"]
list5 = [item.upper() for item in animal]
print(list5)


""" List Comprehension with Nested List"""
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print([item for row in matrix for item in row])


"""List Comprehension with Set and Dictionary
Comprehensions"""
#Set Comprehension
unique_no = { x for x in [1, 2, 3, 3, 5, 4, 2, 4, 3]}
print(unique_no)