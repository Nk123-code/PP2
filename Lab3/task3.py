h = int(input("head:"))
l = int(input("Legs: "))
 
R = int() # кролик
K = int() # кур

for x in range(1, h):
    if x * 2 + (h - x) * 4 == l:
        R = h - x
        K = x

print(R , K)