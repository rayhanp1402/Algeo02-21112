import numpy as np
import math

def PolynomialMultiplication(pol1, pol2):
    max_order = (len(pol1) + len(pol2)) - 1
    arr = [0 for i in range(max_order)]

    for i in range(len(pol1)-1, -1, -1):
        for j in range(len(pol2)-1, -1, -1):
            idx = i + j
            arr[idx] += (pol1[i] * pol2[j])

def Eigenvalue(Matrix):
    if(Matrix.shape[0] == 1): # Basis
        return Matrix[0, 0]
    else:
        Matrix2 = np.zeros(shape=(Matrix.shape[0]-1, Matrix.shape[1]-1), dtype=object)

        for i in range(Matrix.shape[1]):            # Rekursi
            m = 0
            for j in range(1, Matrix.shape[0]):
                n = 0
                for k in range(Matrix.shape[1]):
                    if(i != k):
                        Matrix2[m, n] = Matrix[j, k]
                        n += 1
                m += 1
            
            if(i % 2 == 0):
                print(Matrix[0, 1])
                res = PolynomialMultiplication(Matrix[0, i], Eigenvalue(Matrix2))
            else:
                print(Matrix[0, 1])
                res = PolynomialMultiplication(Matrix[0, i], Eigenvalue(Matrix2))

        return res
                        






a = np.matrix([[-1, 3, 2], 
               [5, 4, -10], 
               [2, 1, 0]])

b = np.matrix([[[-3, 1], [2], [0]], 
               [[2], [-3, 1], [0]], 
               [[0], [0], [-5, 1]]])

print(Eigenvalue(b))