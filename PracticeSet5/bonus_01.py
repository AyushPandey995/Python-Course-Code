print('After adding no. type "N" to stop')
num = []
while True:
    a = input("Enter no-")
    if a.upper() == "N":
        break
    num.append(int(a))
print(num)
s = set(num)
num = list(s)
print(num)

