def isidentity(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if i==j and sqmat[i][j]!=1:
                return False
            elif i!=j and sqmat[i][j]!=0:
                return False
    return True

m0 = [[ 1, 9,  5, 11],
      [ 9, 4,  7,  3],
      [ 5, 7, -7,  8],
      [11, 3,  8,  6]]

m1 = [[ 1, 0,  0, 0],
      [ 0, 1,  0, 0],
      [ 0, 0,  1, 0],
      [ 0, 0,  0, 1]]
print(isidentity(m0))
print(isidentity(m1))