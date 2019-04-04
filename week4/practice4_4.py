def insertionsort(ns):
    def loop(ns,ss):
        print("ns :", ns, "\t\tss :", ss)
        if ns != []:
            tmp = min(ns)
            ns.remove(tmp)
            ns2 = ns[:]
            return loop(ns2, ss+[tmp])
        else:
            return ss
    return loop(ns,[])

print(insertionsort([3,5,4,2]))
