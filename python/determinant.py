# my solution
def minor(i, mat):
    return [row[1:] for row in mat[:i] + mat[i+1:]]
def determinant(mat):
    lgth = len(mat)
    if lgth == 1:
        return mat[0][0]
    return sum((-1) ** i * mat[i][0] * determinant(minor(i,mat)) for i in range(lgth))

# gay solution
# import numpy as np
# def determinant(mat):
#     return np.linalg.det(mat).round()


# check
m1 = [[2, 5, 3], 
      [1,-2,-1], 
      [1, 3, 4]]
print(determinant(m1))


