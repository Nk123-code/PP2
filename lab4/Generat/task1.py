x = int(input()) + 1
a = [i**2 for i in range(1, x) if i **2 <= x]
for i in a:
    print(i, end=" ")
