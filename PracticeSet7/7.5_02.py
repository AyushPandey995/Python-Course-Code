class NegativeNumberError(Exception):
    pass
while True:
    try:
        num = int(input("Enter first number: "))

        if num < 0:
            raise NegativeNumberError("Entered number can not be negative for this program")
        
        print(num)
        break
        
    except ZeroDivisionError as e:
        print("Divisor can not be Zero")

    except Exception as e:
        print(e)
    

    
