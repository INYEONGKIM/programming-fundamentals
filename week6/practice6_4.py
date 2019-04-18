def transpose(mat):
    no_of_columns = len(mat[0])
    no_of_rows = len(mat)
    transposed = []
    for i in range(no_of_columns):
        for j in range(no_of_rows):
            if j==0: transposed.append([])
            transposed[i].append(mat[j][i])
    return transposed

print(transpose([[1,2],
                 [3,4],
                 [5,6]]))