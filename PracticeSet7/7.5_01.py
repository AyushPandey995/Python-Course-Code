while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        print(num1/num2) 

    except ZeroDivisionError as e:
        print("Divisor can not be Zero")

    except Exception as e:
        print(e)
    


