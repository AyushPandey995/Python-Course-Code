###if_elif_else statement
age = int(input("Enter your age- "))

if(age>=18):
    print("You can drive")
elif(age == 0):
    print("Are you kidding")
else:
    print("You cannot drive")


###match statement
num = int(input('Enter a number between 1 and 15- '))

match num :
    case 7:
        print("You Won an Iphone")
    case 13:
        print("You Won a Camera")
    case _:
        print("Better luck next time....")