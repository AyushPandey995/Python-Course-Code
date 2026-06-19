import argparse

parser = argparse.ArgumentParser(description= "Simple Calculator")

parser.add_argument("num1", type= float, help= "Enter first number: ")
parser.add_argument("num2", type= float, help= "Enter second number: ")
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help= "Operation to perform")
args = parser.parse_args()
print(parser)
print(args)

if args.operation == "add":
    print(f"{args.num1} + {args.num2} = {args.num1 + args.num2 }")    
elif args.operation == "subtract":
    print(f"{args.num1} - {args.num2} = {args.num1 - args.num2 }")
elif args.operation == "divide":
    print(f"{args.num1} / {args.num2} = {args.num1 / args.num2 }")
elif args.operation == "multiply":
    print(f"{args.num1} x {args.num2} = {args.num1 * args.num2 }")
else:
    print("Enter valid option")

"""type 'python .\07_argparse.py 5 8 add' in terminal to execute the code"""