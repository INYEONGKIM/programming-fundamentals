def insert(n,ss):
    left = []
    while ss != []:
        if n <= ss[0]:
            return left+[n]+ss
        else:
            ss, left = ss[1:], left+[ss[0]]
    return left+[n]+ss

# print(insert(1,[2,4,5,7,8]))
# print(insert(6,[2,4,5,7,8]))
# print(insert(9,[2,4,5,7,8]))