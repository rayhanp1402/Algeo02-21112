import numpy as np
import math

def CreateLambdaMatrix(Matrix):
    Matrix1 = [[0 for j in range(len(Matrix))] for i in range(len(Matrix))] 

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if(i == j):
                Matrix1[i][j] = [-Matrix[i][j], 1]
            else:
                Matrix1[i][j] = [-Matrix[i][j]]

    return Matrix1

def PolynomialAddition(pol1, pol2):
    if(len(pol1) >= len(pol2)):
        for i in range(len(pol2)):
            pol1[i] += pol2[i]

        return pol1
    else:
        for i in range(len(pol1)):
            pol2[i] += pol1[i]

        return pol2

def PolynomialSubtraction(pol1, pol2):
    if(len(pol1) >= len(pol2)):
        for i in range(len(pol2)):
            pol1[i] -= pol2[i]

        return pol1
    else:
        for i in range(len(pol1)):
            pol2[i] -= pol1[i]

        return pol2

def PolynomialMultiplication(pol1, pol2):
    max_order = (len(pol1) + len(pol2)) - 1
    res = [0 for i in range(max_order)]

    for i in range(len(pol1)-1, -1, -1):
        for j in range(len(pol2)-1, -1, -1):
            idx = i + j
            res[idx] += (pol1[i] * pol2[j])

    return res

def EigenPolynomial(Matrix):
    if(len(Matrix) == 1): # Basis
        return Matrix[0][0]
    else:
        res = [0]
        Matrix1 = np.zeros(shape=(len(Matrix)-1, len(Matrix)-1), dtype=object)

        for i in range(len(Matrix)):  # Rekurens
            m = 0
            for j in range(1, len(Matrix)):
                n = 0
                for k in range(len(Matrix)):
                    if(i != k):
                        Matrix1[m, n] = Matrix[j][k]
                        n += 1
                m += 1

            if(i % 2 == 0):
                res = PolynomialAddition(res, PolynomialMultiplication(Matrix[0][i], EigenPolynomial(Matrix1)))
            else:
                res = PolynomialSubtraction(res, PolynomialMultiplication(Matrix[0][i], EigenPolynomial(Matrix1)))

        return res

def EigenValue(Matrix):
    eigenP = EigenPolynomial(Matrix)
    eigenP.reverse()

    p = np.poly1d(eigenP)
    return p.r




# Tests

a = ([[3, -2, 0], 
      [-2, 3, 0], 
      [0, 0, 5]])

b = [[3, 0],
     [8, -1]]

c = [[-2, -1],
     [5, 2]]

a1 = CreateLambdaMatrix(a)
b1 = CreateLambdaMatrix(b)
c1 = CreateLambdaMatrix(c)

print("Eigen Value Matriks a: ", EigenValue(a1), '\n')
print("Eigen Value Matriks b: ", EigenValue(b1), '\n')
print("Eigen Value Matriks c, yaitu imajiner: ", EigenValue(c1), '\n')