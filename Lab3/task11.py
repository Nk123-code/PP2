def polin(s):
    if s == s[:: -1]:
        return True
    else:
        return False
    
print(polin(input()))
