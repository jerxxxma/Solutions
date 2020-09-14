# ugly determinant
determinant = lambda m: m[0][0] if len(m) == 1 else sum((-1) ** i * m[i][0] * determinant([row[1:] for row in m[:i] + m[i+1:]]) for i in range(len(m)))
# check
m1 = [[2, 5, 3], 
      [1,-2,-1], 
      [1, 3, 4]]

print(determinant(m1))
