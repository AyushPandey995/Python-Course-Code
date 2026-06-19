# ##If we use try-except the program never crash.
# while True:
#     try:
#         end = input("Want to continue the execution(Enter 'Y' for yes and 'N' for no): ").strip().upper()
#         if end == "Y": 
#             a = int(input("Enter first no.: "))
#             b = int(input("Enter second no.: "))
#             print(f"Sum is {a+b}")
#         elif end == "N":
#             print("Thankyou!!...")
#             break
#         else:
#             print("Read the description before entering something.")
#             continue

#     except Exception as e:
#         print("Enter valid value!!!", e)


# ###Customise error using "raise"
# a = int(input("Enter first no.: "))
# b = int(input("Enter second no.: "))
# if b == 0:
#     raise ZeroDivisionError("Divisor can not be 0")
# print(f"Division is {a/b}")


# ###try-except-else
# try:
#     a = int(input("Enter first no.: "))
#     b = int(input("Enter second no.: "))
#     div = a/b
#     print(div)
# except Exception as e:
#     print(e)
# else: # else is executed when there is no error in try block
#     print("All is good....")


### try-except-finally
try:
    a = int(input("Enter first no.: "))
    b = int(input("Enter second no.: "))
    div = a/b
    print(div)
except Exception as e:
    print(e)
finally: #the cose inside rthe 'finally' always executed no matter whether the try block executes completely or not
    print("This is always executed")

