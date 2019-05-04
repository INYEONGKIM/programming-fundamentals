import random

def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)

    res = []
    res.append(seed)
    res.append(seed[2:] + seed[:2])
    t = [seed[1], seed[0], seed[3], seed[2]]
    res.append(t)
    res.append(t[2:] + seed[:2])

    return res

def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes-=1
    return (board, holeset)

board = create_board()
print(make_holes(board, 3))