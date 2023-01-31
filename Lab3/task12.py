def  histogram(l = list()):
    for x in l:
        x = int(x)
        for i in range(x):
            print('*', end='')
        print()

histogram([4,5,7])