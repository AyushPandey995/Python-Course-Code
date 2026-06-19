with open("JohnDoeInfo.txt", "r") as f:
    content = f.read()
    print(content)
    ## Here we don't have to close the file manually as it is done by default.
