def issymmetric(mat):
    count = 0
    size = len(mat)
    for i in range(size):
        for j in range(i+1,size):
            count += 1 # count = count + 1 의 다른 표현
            if mat[i][j] != mat[j][i]:
                return False
    print(count,"번 비교")
    return True

m0 = [[ 1, 9,  5, 11],
      [ 9, 4,  7,  3],
      [ 5, 7, -7,  8],
      [11, 3,  8,  6]]
print(issymmetric(m0))