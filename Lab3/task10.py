def unik_list(l):
    l1 = list()
    for x in l:
        if x not in l1:
            l1.append(x)
    return l1

print(unik_list(input("Lists: ")))