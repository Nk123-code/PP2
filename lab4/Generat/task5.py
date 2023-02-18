def minus(n):
    for i in range(n, 1):
        yield i

def plus(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

if n >= 0:
    a = plus(n) 
else:
    a = minus(n)

for i in a: print(i)