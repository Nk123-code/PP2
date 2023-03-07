import os

if os.access("file name", os.F_OK):
    print(True)
    print(os.access("file name", os.R_OK))
    print(os.access("file name", os.W_OK))
    print(os.access("file name", os.X_OK))

else:
    print(False)