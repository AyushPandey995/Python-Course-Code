a = int(input("Enter first no.-"))
b = int(input("Enter second no.-"))
print("""
Enter '1' for Addition.
Enter '2' for Subtraction.
Enter '3' for Multiplication.
Enter '4' for Division
""")
op = int(input("Enter Your Choice: "))
match op:
    case 1:
        print("Addition - ", a+b)
    case 2:
        print("Subtraction - ", a+b)
    case 3:
        print("Multiplication - ", a+b)
    case 1:
        print("Divison - ", a+b)
    case _:
        print("Enter valid choice")