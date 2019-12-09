import numpy as np

def if_ortho_matrix(A):
    (m, n) = A.shape  # m--rows, n--colomns
    result = True
    for i in range(m):
        for j in range(n):
            production = np.dot(A[i], A[:,j])
            if(i == j):
                if(production != 1.0):
                    result = False
                    print("a , %f",production)
                    break
            else:
                if(production != 0.0):
                    result = False
                    print("a , %f",production)
                    break
    return result

A = np.array([[2.0, 2.0, -1.0],[2.0, -1.0, 2.0],[-1.0, 2.0, 2.0]])
A = A/3
r = if_ortho_matrix(A)
print(r)

