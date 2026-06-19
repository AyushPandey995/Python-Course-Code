f = open("myinfo.txt", "r")
content = f.read()
print(content)
f.close()

"""If the file does not exist then an error occur, to avoid the error we use try-except."""

try :
    f = open("mynfo.txt", "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError as e:
    print("Check the file as no such directory found.")


"""read file line by line"""
try :
    f = open("myinfo.txt", "r")
    for line in f:
        print(line)
except FileNotFoundError as e:
    print("Check the file as no such directory found.")