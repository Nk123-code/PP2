name = input()


with open(name,'a') as fi:
    fi.write(input() + '\n')

with open(name,'r') as fi:
    print(fi.read())