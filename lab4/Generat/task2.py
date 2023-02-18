x = int(input()) + 1
a = [i for i in range(1, x) if i % 2 == 0]
for i in a:
    print(i, end=" ")
