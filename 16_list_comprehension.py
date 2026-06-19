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

