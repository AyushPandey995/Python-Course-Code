# list_1 = [52, 47, 93, 27, 34, 71]
# list_2 = ["Ayush", 143, "Khushi", True, 143.2]

# print(list_1[2])
# print(list_2[2])

# print(list_1[0:3])
# print(list_2[::-1])


### METHODS

marks = [84, 66, 93, 41, 76]
extra_marks = [29, 37, 98, 71]

# marks.append(59)
# print(marks)

marks.pop(3) # if we not insert any index then last element will be poped out
print(marks)

marks.insert(0,31)
print(marks)

marks.extend(extra_marks)
print(marks)

marks.reverse()
print(marks)

marks.remove(93) # in pop we have to insert the index value but in remove method we can directly insert the value or element that we have to remove from the list.  
print(marks)

marks.sort()
print(marks)