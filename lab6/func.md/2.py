s ="ASss"
lo = 0
le = 0
for i in s:
    if i >= 'A' and i <= 'Z':
        lo += 1
    elif i >= 'a' and i <= 'z':
        le += 1
print("Lower;", lo)
print("Letter;", le)