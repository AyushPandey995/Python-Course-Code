num = [10, 11, 12, 13, 14]
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

a = list(filter(even, num))
print(a)