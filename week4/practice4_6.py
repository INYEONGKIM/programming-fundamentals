def insertionsort(s):
    ss=[]
    for i in range(len(s)):
        tmp = min(s)
        s.remove(tmp)
        ss += [tmp]
    return ss+s[:]

print(insertionsort([3,5,4,2]))