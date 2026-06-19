def length(l):

    if len(l)<4:
        return True
    else:
        return False

new = list(filter(length, l := ["python", "rocks", "ai"]))
print(new)

##or

new_list = ["python", "rocks", "ai"]
length = [n for w in new_list if (n := len(w)) < 4]
print(length)