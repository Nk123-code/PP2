def f_gen(m):
     while m >= 1:
         if m % 3 == 0 and m % 4 == 0: yield m
         m -= 1

a = f_gen(int(input()))
for i in a:
    print(i)