def has_33(l):
    for x in range(len(l) - 1):
        if l[x] == '3' and l[x + 1] == '3':
            return True
    return False

print(has_33(list(input())))