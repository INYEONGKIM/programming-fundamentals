def insert(n,ss):
    if ss != []:
        if n <= ss[0]:
            return [n]+ss
        else:
            return [ss[0]] + insert(n,ss[1:])
    else:
        return [n]