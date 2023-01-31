def prime_chek(a):
    for x in range(2,a):
            if a % x == 0:
                return False
    return True

l = list()
def prime_nambers(lists):
    for i in lists:
        if prime_chek(i):
             l.append(i)
    return l

print(prime_nambers([1, 2, 3, 4, 5, 6, 7, 8]))