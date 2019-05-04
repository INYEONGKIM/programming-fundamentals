def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])

    for row in board:
        for i in range(len(row)):
            transposed[i].append(row[i])
    return transposed

board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(transpose(board))