import os

name = input()

if os.path.exists(name):
    os.remove(name)
else:
    print("We dont have this file")