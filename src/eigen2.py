import numpy as np
import math

def matrixMultiplication(Matrix1, Matrix2):
    sum = 0
    resMatrix = [[0 for j in range(len(Matrix1))] for i in range(len(Matrix1))]
    for i in range(len(Matrix1)):
        for j in range(len(Matrix1)):
            for k in range(len(Matrix1)):
                sum += Matrix1[i][k] * Matrix2[k][j]
            resMatrix[i][j] = sum
            sum = 0
    
    return resMatrix



def vectorSubtraction(vector1, vector2):
    res = []
    for i in range(len(vector1)):
        res.append(vector1[i] - vector2[i])

    return res



def multiplyByScalar(scalar, vector):
    resVector = []
    for i in range(len(vector)):
        resVector.append(vector[i] * scalar)

    return resVector



def dotProduct(vector1, vector2):
    res = 0
    for i in range(len(vector1)):
        res += vector1[i] * vector2[i]

    return res



def normalize(vector):
    length = 0
    for i in range(len(vector)):
        length += (vector[i] ** 2)
    
    length = math.sqrt(length)

    resVector = []
    
    for i in range(len(vector)):
        resVector.append(vector[i] / length)

    return resVector



def qrDecomp(Matrix):
    a = []
    u = []
    e = []

    # Store all column Matrix to array a
    temp = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            temp.append(Matrix[j][i])
        a.append(temp)
        temp = []

    # Gram-Schmidt Procedure
    u.append(a[0])              # u1
    e.append(normalize(a[0]))   # e1

    # For un and en, n > 1
    for i in range(1, len(a)):
        temp = a[i]
        for j in range(i):
            temp = vectorSubtraction(temp, multiplyByScalar(dotProduct(a[i], e[j]), e[j]))
        u.append(temp)
        e.append(normalize(u[i]))

    # Q and R matrices
    Q = [[0 for j in range(len(Matrix))] for i in range(len(Matrix))]
    R = [[0 for j in range(len(Matrix))] for i in range(len(Matrix))]

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            Q[j][i] = e[i][j]

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if(i <= j):
                R[i][j] = dotProduct(a[j], e[i])

    return (Q, R)



def eigenValue(Matrix): # Note : Call eigenValue(Matrix)[0] to return only the eigenvalues
    eigenVal = []

    # Create Identity Matrix
    QQ = [[0 for j in range(len(Matrix))] for i in range(len(Matrix))]
    for i in range(len(Matrix)):
        QQ[i][i] = 1

    # Matrix will converge as iteration approaches infinity (large number in practice)
    for i in range(100):
        Q, R = qrDecomp(Matrix)
        Matrix = matrixMultiplication(R, Q)
        QQ = matrixMultiplication(QQ, Q)

    for i in range(len(Matrix)):
        eigenVal.append(Matrix[i][i])

    return (eigenVal, QQ)



def eigenVector(Matrix):
    eigenVecMatrix = eigenValue(Matrix)[1]

    eigenVecMatrix = np.matrix(eigenVecMatrix)

    return eigenVecMatrix






# TESTS
# Samples
# a = ([[0, 0, -2], 
#      [1, 2, 1], 
#      [1, 0, 3]])

# b = [[3, 0],
#     [8, -1]]


# c= [[10, 0, 2],
#    [0, 10, 4],
#    [2, 4, 2]]

# d = [[24294.3, 23763.3, -22564, -27522, 2028.72],         
#     [23763.3, 37215.3, -26584, -31211, -3183.3],         
#     [-22564, -26584, 32686.9, 25780.3, -9319.5],       
#     [-27522, -31211, 25780.3, 45872.7, -12919],       
#     [2028.72, -3183.3, -9319.5, -12919, 23393.1]]

# e = [[2, 1, 0],
#     [1, 2, 0],
#     [0, 0, 3],]

# f = [[1, 1, 1, 1, 1],
#     [16, 8, 4, 2, 1],
#     [81, 27, 9, 3, 1],
#     [256, 64, 16, 4, 1],
#     [625, 125, 25, 5, 1]]



# # Eigen Values
# print("Test Eigen Values :")
# print("Eigen Value Matriks a: ", eigenValue(a)[0])
# print("Eigen Value Matriks b: ", eigenValue(b)[0])
# print("Eigen Value Matriks c: ", eigenValue(c)[0])
# print("Eigen Value Matriks d: ", eigenValue(d)[0])
# print("Eigen Value Matriks e: ", eigenValue(e)[0])
# print("Eigen Value Matriks f: ", eigenValue(f)[0], '\n')



# # Eigen Vectors
# print("Test Eigen Values :")
# print("Eigen Vector Matriks b:\n", (eigenVector(b)), '\n')
# print("Eigen Vector Matriks d:\n", (eigenVector(d)), '\n')