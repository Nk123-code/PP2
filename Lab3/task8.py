def seven(l):
    s =''.join(l)
    if '007' in s:
        return True
    else:
        return False

print(seven(input())) 