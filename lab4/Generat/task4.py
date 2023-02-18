def squares(b,a):
    for i in range(b ,a):
        yield i**2

a = squares(int(input()), int(input()))

for i in a:print(i)