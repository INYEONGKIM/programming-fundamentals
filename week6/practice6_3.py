def issudoku(mat):
    size = len(mat)
    x = [False for _ in range(size*size)]
    for i in range(size):
        for j in range(size):
            if 0 <= mat[i][j]-1 < size*size:
                if x[mat[i][j]-1]:
                    return False
                else:
                    x[mat[i][j] - 1] = True
            else:
                return False
    return True


m0 = [[ 1, 9,  5, 11],
      [ 9, 4,  7,  3],
      [ 5, 7, -7,  8],
      [11, 3,  8,  6]]

m1 = [[ 1, 2,  3],
      [ 5, 4,  6],
      [ 9, 7,  8]]

print(issudoku(m0))
print(issudoku(m1))