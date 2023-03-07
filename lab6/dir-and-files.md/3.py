import os
n = input()
if os.path.exists(n):
    print(os.listdir(n))
else:
    print(False)