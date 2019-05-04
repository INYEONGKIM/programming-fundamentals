import random

def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)

    res = []
    res.append(seed)
    res.append(seed[2:] + seed[:2])
    t = [seed[1], seed[0], seed[3], seed[2]]
    res.append(t)
    res.append(t[2:] + t[:2])

    return res

print(create_board())