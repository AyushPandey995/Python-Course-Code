# num = int(input("Enter a no.: "))
# if(num >=10):
#     print("No. is not in one digit")
# else:
#     print("No. is in one digit")


"""using walrus operator ':=' """

if (new_num := int(input("Enter a no.: "))) >= 10:
    print("No. is not in one digit")
else:
    print("No. is in one digit")
