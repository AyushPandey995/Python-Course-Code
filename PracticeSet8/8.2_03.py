with open("tasks.txt", "r") as f:
    for line in f.readlines():
        print(line)

###or
with open("tasks.txt", "r") as f:
    print(f.read())
