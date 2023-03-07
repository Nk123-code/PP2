with open('file1', 'r') as f1:
    s = f1.read()

with open('file2','w') as f2:
    f2.write(s)

