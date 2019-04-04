def insert(n,ss):
    def loop(ss,left):
        if ss != []:
            if n <= ss[0]:
                return left+[n]+ss
            else:
                return loop(ss[1:], left+[ss[0]])
        else:
            return left+[n]
    return loop(ss,[])

print(insert(1,[2,4,5,7,8]))
print(insert(6,[2,4,5,7,8]))
print(insert(9,[2,4,5,7,8]))