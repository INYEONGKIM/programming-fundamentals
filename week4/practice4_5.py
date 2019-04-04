def insertionsort(ns) :
    ss = []
    while ns != []:
        tmp=min(ns)
        ns.remove(tmp)
        ns2 = ns[:]
        ns, ss = ns2, ss+[tmp]
    return ss


print(insertionsort([3,5,4,2]))