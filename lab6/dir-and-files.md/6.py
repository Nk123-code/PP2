import os
ch = 'A'

# # for i in range(26):
#     s = chr(ord(ch) + i) + '.txt'
#     f = open(s,'a')
#     f.close()

for i in range(26):
    s = chr(ord(ch) + i) + '.txt'
    os.remove(s)
