def bubblesort(ns):
    for k in range(len(ns)-1):
        for i in range(len(ns)-k-1):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

print(bubblesort([32,23,18,7,11,99,55]))